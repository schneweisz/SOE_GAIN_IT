"""
Gyakorlat 2 - Starter file

Feladat:
- file filtering by extension
- file filtering by name substring
- directory statistics
- sorting results
"""

import argparse
import os


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


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
    """Collect files from the directory."""
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
    """Return useful information about one file."""
    file_name = os.path.basename(file_path)

    extension = os.path.splitext(file_name)[1].lower()
    size = os.path.getsize(file_path)
    relative_path = os.path.relpath(file_path, base_path)
    full_path = os.path.abspath(file_path)

    return {
        "name": file_name,
        "extension": extension,
        "size": size,
        "relative_path": relative_path,
        "full_path": full_path,
    }


def matches_filters(file_info, extension=None, name_part=None):
    """Return True if the file matches the active filters."""
    if extension and file_info["extension"] != extension:
        return False

    if name_part and name_part.lower() not in file_info["name"].lower():
        return False

    return True


def count_by_extension(file_infos):
    """Count files by extension."""
    counts = {}

    for file_info in file_infos:
        extension = file_info["extension"] or "(no extension)"
        counts[extension] = counts.get(extension, 0) + 1

    return counts


def print_results(matching_files):
    print_section("RESULTS")

    if not matching_files:
        print("No matching files found.")
        return

    for file_info in matching_files:
        print(
            f"{file_info['relative_path']} "
            f"({file_info['extension'] or 'no extension'}, "
            f"{format_size(file_info['size'])})"
        )


def print_statistics(all_files, matching_files):
    print_section("DIRECTORY STATISTICS")

    total_size = sum(file_info["size"] for file_info in all_files)
    matching_size = sum(file_info["size"] for file_info in matching_files)

    print(f"All files: {len(all_files)}")
    print(f"Matching files: {len(matching_files)}")
    print(f"Total size: {format_size(total_size)}")
    print(f"Matching size: {format_size(matching_size)}")

    if matching_files:
        largest_match = max(matching_files, key=lambda file_info: file_info["size"])
        print(
            "Largest match: "
            f"{largest_match['relative_path']} "
            f"({format_size(largest_match['size'])})"
        )
    else:
        print("Largest match: none")


def print_extension_counts(all_files):
    print_section("EXTENSION COUNTS")

    counts = count_by_extension(all_files)

    if not counts:
        print("No files found.")
        return

    for extension, count in sorted(counts.items()):
        print(f"{extension}: {count}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Starter for Gyakorlat 2: file filtering and directory statistics."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory path to inspect. Default: current directory.",
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
        "-r",
        "--recursive",
        action="store_true",
        help="Search subdirectories too.",
    )
    parser.add_argument(
        "--sort",
        choices=["name", "size", "extension"],
        default="name",
        help="Sort results by this field.",
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

    extension = None
    if args.extension:
        extension = normalize_extension(args.extension)

    file_paths = collect_files(target_path, recursive=args.recursive)
    all_files = [build_file_info(path, target_path) for path in file_paths]

    matching_files = [
        file_info
        for file_info in all_files
        if matches_filters(file_info, extension=extension, name_part=args.name)
    ]

    if args.sort == "name":
        matching_files.sort(key=lambda file_info: file_info["name"].lower())
    elif args.sort == "size":
        matching_files.sort(key=lambda file_info: file_info["size"])
    elif args.sort == "extension":
        matching_files.sort(
            key=lambda file_info: (
                file_info["extension"],
                file_info["name"].lower(),
            )
        )

    print_results(matching_files)
    print_statistics(all_files, matching_files)
    print_extension_counts(all_files)


if __name__ == "__main__":
    main()
