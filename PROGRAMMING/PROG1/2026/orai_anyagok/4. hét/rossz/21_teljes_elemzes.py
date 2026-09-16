scores = [56, 72, 89, 45, 90, 100, 67]


def elemzes_rosszul(values):
    total = 0
    count = 0
    fail_count = 1 #rossz kezdőérték

    for score in values:
        total += score
        count += 1
        if score < 50:
            fail_count += 1

    average = total / fail_count #rossz osztó!
    return {
        "osszes": count,
        "bukas": fail_count,
        "atlag": average,
    }


if __name__ == "__main__":
    print(elemzes_rosszul(scores))
