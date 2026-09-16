values = [10, 20, 30, 5, 100]


def van_10_alatti(values):
    for v in values:
        if v < 10:
            return True
    return False


if __name__ == "__main__":
    print("Van 10 alatti? (hibás)", van_10_alatti(values))
