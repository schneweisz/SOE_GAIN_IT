scores = [56, 72, 89, 45, 90, 100, 67]


def sikeresek(values):
    out=[]
    for score in values:
        if score>=50:
            out.append(score)
    return out


if __name__ == "__main__":
    passed=sikeresek(scores)
    print("Sikeresek:", passed)
    print("Eredeti változatlan:",scores)
