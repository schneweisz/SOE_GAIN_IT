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
    """TODO: Convert file size to a readable string."""
    # TODO:
    # Ha a size nagyobb mint 1024 * 1024, legyen MB.
    # Ha a size nagyobb mint 1024, legyen KB.
    # Kulonben maradjon B.
    return f"{size_in_bytes} B"


def normalize_extension(extension):
    """TODO: Accept both 'txt' and '.txt'."""
    # TODO:
    # 1. alakitsd kisbetusse
    # 2. ha nem ponttal kezdodik, tegyel ele pontot
    return extension


def collect_files(directory_path, recursive=False):
    """TODO: Collect files from the directory."""
    files = []

    if recursive:
        # TODO:
        # Hasznald az os.walk(directory_path) fuggvenyt.
        # Minden fajlhoz keszits full_path valtozot os.path.join()-nal.
        print("TODO: collect files recursively")
    else:
        # TODO:
        # Hasznald az os.listdir(directory_path) fuggvenyt.
        # Csak a fajlokat tedd bele a files listaba.
        print("TODO: collect direct files")

    return files


def build_file_info(file_path, base_path):
    """TODO: Return useful information about one file."""
    file_name = os.path.basename(file_path)

    # TODO:
    # 1. extension = os.path.splitext(file_name)[1]
    # 2. size = os.path.getsize(file_path)
    # 3. relative_path = os.path.relpath(file_path, base_path)
    # 4. full_path = os.path.abspath(file_path)

    return {
        "name": file_name,
        "extension": "TODO",
        "size": 0,
        "relative_path": file_name,
        "full_path": file_path,
    }


def matches_filters(file_info, extension=None, name_part=None):
    """TODO: Return True if the file matches the active filters."""
    # TODO:
    # Ha van extension filter, csak az azonos kiterjesztesu fajlokat engedd at.
    # Ha van name_part filter, csak azokat engedd at,
    # amelyek neve tartalmazza ezt a reszletet.
    return True


def count_by_extension(file_infos):
    """TODO: Count files by extension."""
    counts = {}

    # TODO:
    # Jarj vegig a file_infos listan.
    # A dictionary kulcsa legyen az extension, az erteke a darabszam.

    return counts


def print_results(matching_files):
    print_section("RESULTS")

    if not matching_files:
        print("No matching files found.")
        return

    # TODO:
    # Ird ki a talalatokat rendezett, olvashato formaban.
    for file_info in matching_files:
        print(file_info)


def print_statistics(all_files, matching_files):
    print_section("DIRECTORY STATISTICS")

    # TODO:
    # Szamold ki:
    # - osszes fajl szama
    # - talalatok szama
    # - osszes fajlmeret
    # - talalatok osszes merete
    # - legnagyobb talalat

    print(f"All files: {len(all_files)}")
    print(f"Matching files: {len(matching_files)}")


def print_extension_counts(all_files):
    print_section("EXTENSION COUNTS")

    counts = count_by_extension(all_files)

    # TODO:
    # Ird ki a counts dictionary tartalmat.
    print(counts)


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

    # TODO:
    # Ellenorizd, hogy target_path letezik-e es directory-e.

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

    # TODO:
    # Rendezd a matching_files listat args.sort alapjan.

    print_results(matching_files)
    print_statistics(all_files, matching_files)
    print_extension_counts(all_files)


if __name__ == "__main__":
    main()
