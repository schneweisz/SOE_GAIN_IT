"""Feladat: szenzor mérések tisztítása + átlag/max számítása.

Javítsd a hibás kódot úgy, hogy:
- None és extrém értékek (pl. 120) ne kerüljenek be a számításba
- üres tiszta lista esetén az átlag legyen None
"""

readings = [
    {"t": "10:00", "temp": 21.0},
    {"t": "10:05", "temp": None},
    {"t": "10:10", "temp": 21.5},
    {"t": "10:15", "temp": 120.0},
    {"t": "10:20", "temp": 22.0},
]


def clean(readings):
    # hiba: in-place törlés iterálás közben
    for r in readings:
        t = r["temp"]
        if t is None or t > 60:
            readings.remove(r)
    return readings


def average(clean_readings):
    # hiba: osztás az eredeti hosszal, és None összeadása lehetséges
    total = 0
    for r in clean_readings:
        total += r["temp"]
    return total / len(readings)


def max_temp(clean_readings):
    # hiba: rossz kezdőérték
    m = 0
    for r in clean_readings:
        if r["temp"] > m:
            m = r["temp"]
    return m


def report(readings):
    c = clean(readings)
    return {
        "count": len(readings),
        "clean_count": len(c),
        "avg": average(c),
        "max": max_temp(c),
    }


if __name__ == "__main__":
    print(report(readings))
