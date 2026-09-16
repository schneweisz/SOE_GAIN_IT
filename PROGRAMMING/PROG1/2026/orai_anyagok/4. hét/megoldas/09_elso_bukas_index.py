scores = [56, 72, 89, 45]


def elso_bukas_index(values):
    for i, v in enumerate(values):
        if v < 50:
            return i
    return None


if __name__ == "__main__":
    print("Első bukás indexe (hibás):", elso_bukas_index([50, 60, 70]))
