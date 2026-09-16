import argparse
import os


def format_size(size_in_bytes):
    """Fájlméretet ad vissza olvasható formában (B / KB / MB)."""
    if size_in_bytes >= 1024 * 1024:
        return f"{size_in_bytes / (1024 * 1024):.1f} MB"
    if size_in_bytes >= 1024:
        return f"{size_in_bytes / 1024:.1f} KB"
    return f"{size_in_bytes} B"


def normalize_extension(extension):
    """Elfogadja a 'txt' és a '.txt' formátumot is, kisbetűre alakít."""
    extension = extension.lower()
    if not extension.startswith("."):
        extension = "." + extension
    return extension


# 2. Fájlok összegyűjtése
def collect_files(directory_path, recursive=False):
    files = []

    if recursive:
        for current_dir, _sub_dirs, file_names in os.walk(directory_path):
            for file_name in file_names:
                full_path = os.path.join(current_dir, file_name)
                files.append(full_path)
    else:
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            if os.path.isfile(full_path):
                files.append(full_path)

    return files


# 3. Fájladatok tárolása
def build_file_info(file_path, base_path):
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1].lower()
    size = os.path.getsize(file_path)
    relative_path = os.path.relpath(file_path, base_path)
    full_path = os.path.abspath(file_path)

    return {
        "name": file_name,
        "extension": extension,
        "size": size,
        "relative_path": relative_path.replace("\\", "/"),
        "full_path": full_path,
    }


# 4. Szűrés
def matches_filters(file_info, extension=None, name_part=None, min_size=None):
    if extension is not None and file_info["extension"] != extension:
        return False

    if name_part is not None and name_part.lower() not in file_info["name"].lower():
        return False

    if min_size is not None and file_info["size"] < min_size:
        return False

    return True


# 5. Rendezés
def sort_files(file_infos, sort_by):
    return sorted(file_infos, key=lambda file_info: file_info[sort_by])


def count_by_extension(file_infos):
    counts = {}
    for file_info in file_infos:
        extension = file_info["extension"] if file_info["extension"] else "(nincs)"
        counts[extension] = counts.get(extension, 0) + 1
    return counts


def find_largest(file_infos):
    if not file_infos:
        return None
    return max(file_infos, key=lambda file_info: file_info["size"])


def build_report_lines(all_files, matching_files, largest_only=False):
    lines = []

    # Plusz kihívás: --largest-only
    if largest_only:
        largest = find_largest(matching_files)
        lines.append("=" * 60)
        lines.append("LEGNAGYOBB TALÁLAT")
        lines.append("=" * 60)
        if largest is None:
            lines.append("Nincs találat.")
        else:
            lines.append(
                f"{largest['relative_path']} | {largest['extension']} | "
                f"{format_size(largest['size'])}"
            )
        return lines

    # 6. Eredmények kiírása
    lines.append("=" * 60)
    lines.append("TALÁLATOK")
    lines.append("=" * 60)
    if not matching_files:
        lines.append("Nincs a feltételnek megfelelő fájl.")
    else:
        for file_info in matching_files:
            lines.append(
                f"{file_info['relative_path']} | {file_info['extension']} | "
                f"{format_size(file_info['size'])}"
            )

    # 7. Statisztika készítése
    lines.append("")
    lines.append("=" * 60)
    lines.append("STATISZTIKA")
    lines.append("=" * 60)

    total_count = len(all_files)
    match_count = len(matching_files)
    total_size = sum(file_info["size"] for file_info in all_files)
    match_size = sum(file_info["size"] for file_info in matching_files)
    largest = find_largest(matching_files)

    lines.append(f"Összes fájl száma: {total_count}")
    lines.append(f"Találatok száma: {match_count}")
    lines.append(f"Összes fájl mérete: {format_size(total_size)}")
    lines.append(f"Találatok összesített mérete: {format_size(match_size)}")
    if largest is None:
        lines.append("Legnagyobb találat: nincs")
    else:
        lines.append(
            f"Legnagyobb találat: {largest['relative_path']} "
            f"({format_size(largest['size'])})"
        )

    lines.append("")
    lines.append("=" * 60)
    lines.append("KITERJESZTÉSENKÉNTI DARABSZÁM")
    lines.append("=" * 60)
    counts = count_by_extension(matching_files)
    if not counts:
        lines.append("Nincs fájl.")
    else:
        for extension, count in sorted(counts.items()):
            lines.append(f"{extension}: {count} db")

    return lines


# 8. Jelentés mentése fájlba
def save_report(lines, save_path):
    """Elmenti a jelentést a megadott fájlba."""
    with open(save_path, "w", encoding="utf-8") as report_file:
        report_file.write("\n".join(lines) + "\n")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fájlok keresése, szűrése, statisztika készítése egy mappában."
    )
    parser.add_argument(
        "path",
        help="A vizsgálandó mappa elérési útja.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Az almappák fájljait is vizsgálja.",
    )
    parser.add_argument(
        "-e",
        "--extension",
        help="Szűrés kiterjesztés alapján. Példa: --extension txt",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Szűrés fájlnévrészlet alapján. Példa: --name report",
    )
    parser.add_argument(
        "--min-size",
        type=int,
        help="Szűrés minimális fájlméret alapján (bájtban). Példa: --min-size 100",
    )
    parser.add_argument(
        "--sort",
        choices=["name", "size", "extension"],
        default="name",
        help="Rendezés mező szerint (name, size, extension). Alapértelmezett: name.",
    )
    parser.add_argument(
        "--save",
        help="A jelentés elmentése a megadott fájlba.",
    )
    # Plusz kihívás
    parser.add_argument(
        "--largest-only",
        action="store_true",
        help="Kizárólag a legnagyobb találatot írja ki.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    # 1. Útvonal ellenőrzése
    target_path = os.path.abspath(args.path)
    print(f"Vizsgált mappa: {target_path}")

    if not os.path.exists(target_path):
        print(f"Hiba: a megadott útvonal nem létezik: {target_path}")
        return

    if not os.path.isdir(target_path):
        print(f"Hiba: a megadott útvonal nem mappa: {target_path}")
        return

    extension = normalize_extension(args.extension) if args.extension else None

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

    matching_files = sort_files(matching_files, args.sort)

    lines = build_report_lines(all_files, matching_files, largest_only=args.largest_only)

    print()
    for line in lines:
        print(line)

    # 8. Jelentés mentése fájlba (opcionális)
    if args.save:
        save_report(lines, args.save)
        print()
        print(f"A jelentés elmentve ide: {os.path.abspath(args.save)}")


if __name__ == "__main__":
    main()
