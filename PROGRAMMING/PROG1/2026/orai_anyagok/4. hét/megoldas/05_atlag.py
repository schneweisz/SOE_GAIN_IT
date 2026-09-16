scores = [51, 52, 53]


def atlag(values):
    if len(values) == 0:
        return None
    total = 0
    for v in values:
        total += v
    return total / len(values) 


if __name__ == "__main__":
    print("Átlag (hibás, //):", atlag(scores))
