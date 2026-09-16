scores = [56, 72, 89, 45, 90, 100, 67, 72, 38, 84, 91, 60, 73, 88, 55, 49]


def van_bukas_rosszul(values):
    found = False
    for score in values:
        if score < 50:
            found = True
    return found

    #nincs korai kilépés!
if __name__ == "__main__":
    print("Van bukás" if van_bukas_rosszul(scores) else "Nincs bukás")
