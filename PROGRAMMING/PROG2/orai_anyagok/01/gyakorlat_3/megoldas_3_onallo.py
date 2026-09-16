"""
Gyakorlat 3 - Onallo megoldas

Feladat:
- fajlok keresese
- szures kiterjesztes, nevreszlet es minimalis meret alapjan
- rendezes
- statisztika keszitese
- jelentes mentese fajlba
"""

import argparse
import os


def format_size(size_in_bytes):
    """Convert file size to a readable string."""
    if size_in_bytes >= 1024 * 1024:
        return f"{size_in_bytes / (1024 * 1024):.2f} MB"

    if size_in_bytes >= 1024:
        return f"{size_in_bytes / 1024:.2f} KB"

    return f"{size_in_bytes} B"


def normalize_extension(extension):
    """Accept both 'txt' and '.txt'."""
    extension = extension.lower()

    if not extension.startswith("."):
        extension = "." + extension

    return extension


def collect_files(directory_path, recursive=False):
    """Collect file paths from a directory."""
    files = []

    if recursive:
        for current_root, dir_names, file_names in os.walk(directory_path):
            dir_names.sort()
            file_names.sort()

            for file_name in file_names:
                full_path = os.path.join(current_root, file_name)
                files.append(full_path)
    else:
        for item_name in sorted(os.listdir(directory_path)):
            full_path = os.path.join(directory_path, item_name)

            if os.path.isfile(full_path):
                files.append(full_path)

    return files


def build_file_info(file_path, base_path):
    """Return useful data about one file."""
    file_name = os.path.basename(file_path)

    return {
        "name": file_name,
        "extension": os.path.splitext(file_name)[1].lower(),
        "size": os.path.getsize(file_path),
        "relative_path": os.path.relpath(file_path, base_path),
        "full_path": os.path.abspath(file_path),
    }


def matches_filters(file_info, extension=None, name_part=None, min_size=None):
    """Return True if the file matches every active filter."""
    if extension and file_info["extension"] != extension:
        return False

    if name_part and name_part.lower() not in file_info["name"].lower():
        return False

    if min_size is not None and file_info["size"] < min_size:
        return False

    return True


def sort_files(file_infos, sort_key):
    """Sort files by the selected field."""
    if sort_key == "name":
        file_infos.sort(key=lambda file_info: file_info["name"].lower())
    elif sort_key == "size":
        file_infos.sort(key=lambda file_info: file_info["size"])
    elif sort_key == "extension":
        file_infos.sort(
            key=lambda file_info: (
                file_info["extension"],
                file_info["name"].lower(),
            )
        )


def count_by_extension(file_infos):
    """Count files by extension."""
    counts = {}

    for file_info in file_infos:
        extension = file_info["extension"] or "(no extension)"
        counts[extension] = counts.get(extension, 0) + 1

    return counts


def build_results_lines(matching_files):
    """Build readable result lines."""
    if not matching_files:
        return ["No matching files found."]

    lines = []

    for file_info in matching_files:
        extension = file_info["extension"] or "no extension"
        size = format_size(file_info["size"])
        lines.append(f"{file_info['relative_path']} | {extension} | {size}")

    return lines


def build_statistics_lines(all_files, matching_files):
    """Build directory statistics lines."""
    total_size = sum(file_info["size"] for file_info in all_files)
    matching_size = sum(file_info["size"] for file_info in matching_files)

    lines = [
        f"All files: {len(all_files)}",
        f"Matching files: {len(matching_files)}",
        f"Total size: {format_size(total_size)}",
        f"Matching size: {format_size(matching_size)}",
    ]

    if matching_files:
        largest_match = max(matching_files, key=lambda file_info: file_info["size"])
        lines.append(
            "Largest match: "
            f"{largest_match['relative_path']} "
            f"({format_size(largest_match['size'])})"
        )
    else:
        lines.append("Largest match: none")

    return lines


def build_extension_count_lines(all_files):
    """Build extension count lines."""
    counts = count_by_extension(all_files)

    if not counts:
        return ["No files found."]

    lines = []

    for extension, count in sorted(counts.items()):
        lines.append(f"{extension}: {count}")

    return lines


def add_section(lines, title, content_lines):
    """Add a formatted section to a report."""
    lines.append("")
    lines.append("=" * 60)
    lines.append(title)
    lines.append("=" * 60)
    lines.extend(content_lines)


def build_report(target_path, all_files, matching_files):
    """Build the full report as a list of lines."""
    lines = [f"Inspected directory: {target_path}"]

    add_section(lines, "RESULTS", build_results_lines(matching_files))
    add_section(lines, "DIRECTORY STATISTICS", build_statistics_lines(all_files, matching_files))
    add_section(lines, "EXTENSION COUNTS", build_extension_count_lines(all_files))

    return lines


def save_report(file_path, report_lines):
    """Save report lines to a text file."""
    with open(file_path, "w", encoding="utf-8") as report_file:
        report_file.write("\n".join(report_lines))
        report_file.write("\n")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Gyakorlat 3: file search, filtering and report generation."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory path to inspect. Default: current directory.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Search subdirectories too.",
    )
    parser.add_argument(
        "-e",
        "--extension",
        help="Filter by extension. Example: --extension txt",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Filter by part of the file name. Example: --name report",
    )
    parser.add_argument(
        "--min-size",
        type=int,
        help="Only show files at least this large, in bytes.",
    )
    parser.add_argument(
        "--sort",
        choices=["name", "size", "extension"],
        default="name",
        help="Sort results by this field.",
    )
    parser.add_argument(
        "--save",
        help="Save the report to this file.",
    )
    parser.add_argument(
        "--largest-only",
        action="store_true",
        help="Show only the largest matching file.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    target_path = os.path.abspath(args.path)

    if not os.path.exists(target_path):
        print(f"Error: path does not exist: {target_path}")
        return

    if not os.path.isdir(target_path):
        print(f"Error: path is not a directory: {target_path}")
        return

    if args.min_size is not None and args.min_size < 0:
        print("Error: --min-size cannot be negative.")
        return

    extension = None
    if args.extension:
        extension = normalize_extension(args.extension)

    file_paths = collect_files(target_path, recursive=args.recursive)
    all_files = [build_file_info(path, target_path) for path in file_paths]

    matching_files = [
        file_info
        for file_info in all_files
        if matches_filters(
            file_info,
            extension=extension,
            name_part=args.name,
            min_size=args.min_size,
        )
    ]

    if args.largest_only and matching_files:
        largest_match = max(matching_files, key=lambda file_info: file_info["size"])
        matching_files = [largest_match]

    sort_files(matching_files, args.sort)

    report_lines = build_report(target_path, all_files, matching_files)

    for line in report_lines:
        print(line)

    if args.save:
        save_report(args.save, report_lines)
        print()
        print(f"Report saved to: {args.save}")


if __name__ == "__main__":
    main()
