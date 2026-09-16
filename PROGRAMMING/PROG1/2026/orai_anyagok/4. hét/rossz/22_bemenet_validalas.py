scores = [56, 72, 89, 45, 90, 100, 67, -1, 101]


def minden_ervenyes_rosszul(values):
    for s in values:
        if s < 0 and s > 100:
            return False
    return True


if __name__ == "__main__":
    print("Minden pontszám 0..100? (hibás)", minden_ervenyes_rosszul(scores))
