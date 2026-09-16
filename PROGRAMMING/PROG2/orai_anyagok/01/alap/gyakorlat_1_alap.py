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
    """TODO: Show basic information about the given path."""
    print_section("PATH BASICS")

    # Ezek segito kiirasok, a tobbit egeszitsd ki.
    print(f"Current working directory (CWD): {os.getcwd()}")
    print(f"Input path: {input_path}")

    # TODO:
    # 1. absolute_path = os.path.abspath(input_path)
    # 2. normalized_path = os.path.normpath(input_path)
    # 3. relative_path = os.path.relpath(absolute_path)
    # 4. basename = os.path.basename(absolute_path)
    # 5. parent_directory = os.path.dirname(absolute_path)
    # 6. exists / is file / is directory ellenorzes
    #
    # Tipp: print() segitsegevel ird ki az eredmenyeket.

    absolute_path = input_path  # TODO: csereld le os.path.abspath(...) hivasra
    return absolute_path


def list_direct_children(directory_path):
    """TODO: List direct files and folders in the given directory."""
    print_section("DIRECT LISTING")

    folders = []
    files = []

    # TODO:
    # 1. jarj vegig a mappa elemein os.listdir(directory_path) segitsegevel
    # 2. minden elemhez keszits full_path valtozot os.path.join()-nal
    # 3. os.path.isdir(full_path) alapjan keruljon a folders listaba
    # 4. os.path.isfile(full_path) alapjan keruljon a files listaba
    # 5. rendezd a listakat abc szerint

    print("Folders / Directories:")
    # TODO: for ciklussal ird ki a folders lista elemeit
    print("  TODO: print folders here")

    print()
    print("Files:")
    # TODO: for ciklussal ird ki a files lista elemeit
    print("  TODO: print files here")

    return folders, files


def show_join_examples(directory_path, folders, files):
    """TODO: Demonstrate os.path.join."""
    print_section("PATH JOIN EXAMPLES")

    # TODO:
    # Valassz ki nehany fajlnevet vagy mappanevet,
    # majd mutasd meg, milyen full path keszul belole.
    example_name = "example.txt"
    example_path = os.path.join(directory_path, example_name)

    print(f"os.path.join(directory_path, '{example_name}')")
    print(f"Result: {example_path}")


def walk_directory(directory_path):
    """TODO: Use os.walk for recursive traversal."""
    print_section("RECURSIVE TREE")

    # TODO:
    # os.walk(directory_path) harom dolgot ad vissza:
    # current_root, dir_names, file_names
    #
    # Pelda:
    # for current_root, dir_names, file_names in os.walk(directory_path):
    #     print(current_root)
    #     print(dir_names)
    #     print(file_names)

    print("TODO: recursive traversal goes here")


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

    # TODO:
    # Mielott listazol, ellenorizd:
    # - letezik-e a target_path
    # - directory-e a target_path

    folders, files = list_direct_children(target_path)
    show_join_examples(target_path, folders, files)

    if args.recursive:
        walk_directory(target_path)


if __name__ == "__main__":
    main()
