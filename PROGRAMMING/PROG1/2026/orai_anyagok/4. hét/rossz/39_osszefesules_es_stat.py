"""Feladat: a két rendezett listát össze kell fésülni, majd min/max/átlagot számolni.

Javítsd a meglévő kódot (ne írj teljesen újat).
"""

a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 9]


def merge_sorted(a, b):
    # hibák: i/j rossz léptetés, és a maradék elemek kimaradnak
    i = 0
    j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            j += 1  # hiba: i helyett j
        else:
            out.append(b[j])
            i += 1  # hiba: j helyett i
    return out


def analyze(values):
    # hibák: rossz kezdőértékek, rossz osztó
    total = 0
    mmin = 0
    mmax = 0
    for v in values:
        total += v
        if v < mmin:
            mmin = v
        if v > mmax:
            mmax = v
    return {"min": mmin, "max": mmax, "avg": total / (len(values) - 1)}


if __name__ == "__main__":
    merged = merge_sorted(a, b)
    print("Merged:", merged)
    print("Stat:", analyze(merged))
