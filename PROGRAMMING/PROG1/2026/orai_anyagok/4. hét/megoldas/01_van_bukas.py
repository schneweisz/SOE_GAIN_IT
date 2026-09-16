scores = [56, 72, 89, 45, 90, 100, 67, 72, 38, 84, 91, 60, 73, 88, 55, 49]


def van_bukas(values):
    for score in values:
        if score < 50:
            return True
    return False


if __name__ == "__main__":
    print("Van bukás" if van_bukas(scores) else "Nincs bukás")
