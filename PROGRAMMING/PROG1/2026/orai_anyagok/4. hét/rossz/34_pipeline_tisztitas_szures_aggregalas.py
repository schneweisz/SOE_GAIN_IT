readings = [
    {"t": "2026-03-03 10:00", "temp": 21.0},
    {"t": "2026-03-03 10:05", "temp": None},
    {"t": "2026-03-03 10:10", "temp": 21.5},
    {"t": "2026-03-03 10:15", "temp": 120.0},
    {"t": "2026-03-03 10:20", "temp": 22.0},
]


def average_temp_rosszul(readings):
    # hibák: nem szűr, és None-nal összead
    total = 0
    for r in readings:
        total += r["temp"]
    return total / len(readings)


if __name__ == "__main__":
    print(average_temp_rosszul(readings))
