readings = [
    {"t": "10:00", "temp": 21.0},
    {"t": "10:05", "temp": None},
    {"t": "10:10", "temp": 21.5},
    {"t": "10:15", "temp": 120.0},
    {"t": "10:20", "temp": 22.0},
    {"t": "10:25", "temp": 19.0},
]


def clean(readings):
    out = []
    for r in readings:
        temp = r.get("temp")
        if isinstance(temp, (int, float)) and 0 <= temp <= 60:
            out.append(r)
    return out


def average(clean_readings):
    if len(clean_readings) == 0:
        return None
    total = 0
    count = 0
    for r in clean_readings:
        total += r["temp"]
        count += 1
    return total / count


def max_temp(clean_readings):
    m = None
    for r in clean_readings:
        t = r["temp"]
        if m is None or t > m:
            m = t
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
