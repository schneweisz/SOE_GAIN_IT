readings = [
    {"t": "2026-03-03 10:00", "temp": 21.0},
    {"t": "2026-03-03 10:05", "temp": None},
    {"t": "2026-03-03 10:10", "temp": 21.5},
    {"t": "2026-03-03 10:15", "temp": 120.0},
    {"t": "2026-03-03 10:20", "temp": 22.0},
]


def clean_readings(readings):
    out = []
    for r in readings:
        temp = r.get("temp")
        if isinstance(temp, (int, float)) and 0 <= temp <= 60:
            out.append(r)
    return out


def average_temp(readings):
    if len(readings) == 0:
        return None
    total = 0
    count = 0
    for r in readings:
        total += r["temp"]
        count += 1
    return total / count


def max_temp(readings):
    m = None
    for r in readings:
        t = r["temp"]
        if m is None or t > m:
            m = t
    return m


if __name__ == "__main__":
    clean = clean_readings(readings)
    print("Tiszta mérések:", clean)
    print("Átlag:", average_temp(clean))
    print("Max:", max_temp(clean))
