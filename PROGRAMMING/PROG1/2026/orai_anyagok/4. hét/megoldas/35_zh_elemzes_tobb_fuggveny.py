scores = [56, 72, 89, 45, 90, 100, 67, 72, 38, 84, 91, 60, 73, 88, 55, 49]


def filter_passed(values):
    out = []
    for v in values:
        if v >= 50:
            out.append(v)
    return out


def count_if(values, predicate):
    c = 0
    for v in values:
        if predicate(v):
            c += 1
    return c


def average(values):
    if len(values) == 0:
        return None
    total = 0
    for v in values:
        total += v
    return total / len(values)


def analyze(values):
    passed = filter_passed(values)
    fail_count = count_if(values, lambda x: x < 50)
    excellent_count = count_if(values, lambda x: x >= 90)

    return {
        "osszes": len(values),
        "bukas": fail_count,
        "sikeres": len(passed),
        "jeles_90plus": excellent_count,
        "atlag": average(values),
        "sikeresek_atlaga": average(passed),
    }


if __name__ == "__main__":
    stats = analyze(scores)
    for k in ["osszes", "bukas", "sikeres", "jeles_90plus", "atlag", "sikeresek_atlaga"]:
        print(f"{k}: {stats[k]}")
