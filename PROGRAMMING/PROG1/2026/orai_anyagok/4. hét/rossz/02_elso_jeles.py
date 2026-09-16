scores = [56, 72, 89, 45, 90, 100, 67]


def elso_jeles_rosszul(values):
    for score in values:
        if score >= 90:
            first = score
            break
    return first
    #hiba: ha nincs találat, a first nincs definiálva

if __name__ == "__main__":
    print(elso_jeles_rosszul([10, 20, 30]))