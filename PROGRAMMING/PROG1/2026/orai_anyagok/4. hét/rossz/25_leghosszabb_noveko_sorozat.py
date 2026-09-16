values = [1, 2, 3, 2, 3, 4, 5, 1, 2]


def longest_increasing_streak_rosszul(values):
    if len(values) == 0:
        return 0

    best = 1
    current = 1
    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current += 1
        else:
            if current > best:
                best = current
            current = 1
    return best


if __name__ == "__main__":
    print(longest_increasing_streak_rosszul(values))
