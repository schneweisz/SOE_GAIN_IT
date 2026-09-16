values = [56, 72, 89, 45, 90, 100, 67]


def minimum(values):
    m = None 
    for v in values:
        if v < m or m is None:
            m = v
    return m


if __name__ == "__main__":
    print("Minimum:", minimum(values))
