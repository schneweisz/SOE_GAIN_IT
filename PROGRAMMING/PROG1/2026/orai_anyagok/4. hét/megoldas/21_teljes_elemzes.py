scores = [56, 72, 89, 45, 90, 100, 67]


def elemzes(values):
    total = 0
    count = 0
    fail_count = 0

    for score in values:
        total += score
        count += 1
        if score < 50:
            fail_count += 1

    average = total / count
    return {
        "osszes": count,
        "bukas": fail_count,
        "atlag": average,
    }


if __name__ == "__main__":
    print(elemzes(scores))
