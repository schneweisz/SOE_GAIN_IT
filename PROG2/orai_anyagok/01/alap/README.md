# Alap fajlok az elso ket gyakorlathoz

Ez a mappa starter valtozatot tartalmaz. Nem kesz megoldas, hanem vaz:

- a fajlok futtathatok,
- a fontos function nevek es programreszek mar megvannak,
- a hianyzo reszek `TODO` kommentekkel vannak jelolve,
- van `minta_mappa`, hogy ne ures mappan kelljen tesztelni.

## Fajlok

- `gyakorlat_1_alap.py`: starter file directory listing es path handling gyakorlashoz.
- `gyakorlat_2_alap.py`: starter file filtering es directory statistics gyakorlashoz.
- `angol_kifejezesek.md`: fontos angol kifejezesek.
- `minta_mappa/`: teszteleshez hasznalhato sample directory.

## Gyakorlat 1 - cel

Keszits programot, amely:

1. kiirja a current working directory erteket,
2. megmutatja a megadott path absolute es relative formajat,
3. ellenorzi, hogy a path exists / is file / is directory,
4. kilistazza a kozvetlen files es folders elemeket,
5. osszeallit teljes eleresi utakat `os.path.join()` segitsegevel,
6. opcionálisan rekurzivan is bejarja a mappat `os.walk()` segitsegevel.

Futtatas:

```bash
python gyakorlat_1_alap.py minta_mappa
python gyakorlat_1_alap.py minta_mappa --recursive
```

## Gyakorlat 2 - cel

Keszits programot, amely:

1. osszegyujti a fajlokat egy megadott directory alatt,
2. tud extension alapjan szurni,
3. tud name substring alapjan szurni,
4. tud size alapjan egyszeru statisztikat kesziteni,
5. megszamolja a fajlokat extension szerint,
6. rendezett formaban jeleniti meg a results listat.

Futtatas:

```bash
python gyakorlat_2_alap.py minta_mappa --recursive
python gyakorlat_2_alap.py minta_mappa --recursive --extension txt
python gyakorlat_2_alap.py minta_mappa --recursive --name report
```

## Tipp

A teljes, kidolgozott valtozat a `../megoldas` mappaban van.
