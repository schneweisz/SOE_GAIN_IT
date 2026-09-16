scores = [56, 72, 89, 45, 90, 100, 67]


def elso_jeles(values):
    for score in values:
        if score >= 90:
            return score
    return None

if __name__ == "__main__":
    print(elso_jeles(scores))