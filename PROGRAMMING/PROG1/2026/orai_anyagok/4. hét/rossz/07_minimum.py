values = [56, 72, 89, 45, 90, 100, 67]


def minimum_rosszul(values):
    m = 0 
    for v in values:
        if v < m:
            m = v
    return m


if __name__ == "__main__":
    print("Minimum (hibás):", minimum_rosszul(values))
