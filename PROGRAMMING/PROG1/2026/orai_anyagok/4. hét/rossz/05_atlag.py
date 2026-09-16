scores = [51, 52, 53]


def atlag_rosszul(values):
    total = 0
    for v in values:
        total += v
    return total // len(values) 


if __name__ == "__main__":
    print("Átlag (hibás, //):", atlag_rosszul(scores))
