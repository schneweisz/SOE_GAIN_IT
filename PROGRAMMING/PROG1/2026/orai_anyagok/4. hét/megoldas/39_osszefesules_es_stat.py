a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 9]


def merge_sorted(a, b):
    i = 0
    j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    while i < len(a):
        out.append(a[i])
        i += 1
    while j < len(b):
        out.append(b[j])
        j += 1
    return out


def analyze(values):
    if len(values) == 0:
        return {"min": None, "max": None, "avg": None}
    total = 0
    mmin = values[0]
    mmax = values[0]
    for v in values:
        total += v
        if v < mmin:
            mmin = v
        if v > mmax:
            mmax = v
    return {"min": mmin, "max": mmax, "avg": total / len(values)}


if __name__ == "__main__":
    merged = merge_sorted(a, b)
    print("Merged:", merged)
    print("Stat:", analyze(merged))
