"""Feladat: ez a script egy ZH-pontlista elemzését szeretné kiírni.

Ne írj új programot: javítsd a meglévőt.
Tipp: kezdőértékek, üres lista, rossz feltételek, rossz osztó, mellékhatás.
"""

scores = [56, 72, 89, 45, 90, 100, 67, 72, 38, 84, 91, 60, 73, 88, 55, 49]


def filter_passed(values):
    # hiba: mellékhatás (az eredetit módosítja), és közben hibásan iterál
    for v in values:
        if v < 50:
            values.remove(v)
    return values


def count_if(values, predicate):
    # hiba: rossz kezdőérték
    c = 1
    for v in values:
        if predicate(v):
            c += 1
    return c


def average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)  # hiba: üres listán ZeroDivisionError


def analyze(values):
    passed = filter_passed(values)

    # hiba: rossz feltételek
    fail_count = count_if(values, lambda x: x <= 50)
    excellent_count = count_if(values, lambda x: x > 90)

    # hiba: sikeresek száma rosszul számolódik (eredeti hossza)
    return {
        "osszes": len(values),
        "bukas": fail_count,
        "sikeres": len(values),
        "jeles_90plus": excellent_count,
        "atlag": average(values),
        "sikeresek_atlaga": average(passed),
    }


if __name__ == "__main__":
    stats = analyze(scores)
    for k in stats:
        print(k, stats[k])
