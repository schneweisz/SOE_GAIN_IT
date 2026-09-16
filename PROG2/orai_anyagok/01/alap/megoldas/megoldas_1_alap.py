"""
Gyakorlat 1 - Starter file

Feladat:
- current working directory (CWD) kiirasa
- absolute path / relative path kezelese
- files es folders listazasa
- path join gyakorlas
- optional recursive traversal
"""

import argparse
import os


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def show_path_basics(input_path):
    """Show basic information about the given path."""
    print_section("PATH BASICS")

    # Ezek segito kiirasok, a tobbit egeszitsd ki.
    print(f"Current working directory (CWD): {os.getcwd()}")
    print(f"Input path: {input_path}")

    absolute_path = os.path.abspath(input_path)
    normalized_path = os.path.normpath(input_path)
    relative_path = os.path.relpath(absolute_path)
    basename = os.path.basename(absolute_path)
    parent_directory = os.path.dirname(absolute_path)

    print(f"Absolute path: {absolute_path}")
    print(f"Normalized path: {normalized_path}")
    print(f"Relative path from CWD: {relative_path}")
    print(f"Basename: {basename}")
    print(f"Parent directory: {parent_directory}")
    print(f"Exists: {os.path.exists(absolute_path)}")
    print(f"Is file: {os.path.isfile(absolute_path)}")
    print(f"Is directory: {os.path.isdir(absolute_path)}")

    return absolute_path


def list_direct_children(directory_path):
    """List direct files and folders in the given directory."""
    print_section("DIRECT LISTING")

    folders = []
    files = []

    for item_name in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item_name)

        if os.path.isdir(full_path):
            folders.append(item_name)
        elif os.path.isfile(full_path):
            files.append(item_name)

    folders.sort()
    files.sort()

    print("Folders / Directories:")
    if folders:
        for folder in folders:
            print(f"  {folder}")
    else:
        print("  (no folders)")

    print()
    print("Files:")
    if files:
        for file_name in files:
            print(f"  {file_name}")
    else:
        print("  (no files)")

    return folders, files


def show_join_examples(directory_path, folders, files):
    """Demonstrate os.path.join."""
    print_section("PATH JOIN EXAMPLES")

    example_names = folders[:2] + files[:2]

    if not example_names:
        example_names = ["example.txt"]

    for example_name in example_names:
        example_path = os.path.join(directory_path, example_name)
        print(f"os.path.join(directory_path, '{example_name}')")
        print(f"Result: {example_path}")
        print()


def walk_directory(directory_path):
    """Use os.walk for recursive traversal."""
    print_section("RECURSIVE TREE")

    base_depth = directory_path.rstrip(os.sep).count(os.sep)

    for current_root, dir_names, file_names in os.walk(directory_path):
        dir_names.sort()
        file_names.sort()

        current_depth = current_root.rstrip(os.sep).count(os.sep) - base_depth
        indent = "  " * current_depth
        print(f"{indent}{os.path.basename(current_root) or current_root}/")

        file_indent = "  " * (current_depth + 1)
        for file_name in file_names:
            print(f"{file_indent}{file_name}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Starter for Gyakorlat 1: directory listing and path handling."
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
        help="Use os.walk to show the full directory tree.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    target_path = show_path_basics(args.path)

    if not os.path.exists(target_path):
        print()
        print(f"Error: path does not exist: {target_path}")
        return

    if not os.path.isdir(target_path):
        print()
        print(f"Error: path is not a directory: {target_path}")
        return

    folders, files = list_direct_children(target_path)
    show_join_examples(target_path, folders, files)

    if args.recursive:
        walk_directory(target_path)


if __name__ == "__main__":
    main()
