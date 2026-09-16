values = [56, 72, 89, 45]


def osszeg_off_by_one(values):
    total = 0
    for i in range(len(values)):  
        total += values[i]
    return total


if __name__ == "__main__":
    print(osszeg_off_by_one(values))
