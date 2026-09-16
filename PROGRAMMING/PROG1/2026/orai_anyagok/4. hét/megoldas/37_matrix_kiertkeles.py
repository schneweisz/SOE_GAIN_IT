matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


def is_rectangular(matrix):
    if len(matrix) == 0:
        return True
    w = len(matrix[0])
    for row in matrix:
        if len(row) != w:
            return False
    return True


def row_sums(matrix):
    sums = []
    for row in matrix:
        s = 0
        for v in row:
            s += v
        sums.append(s)
    return sums


def col_sums(matrix):
    if len(matrix) == 0:
        return []
    if not is_rectangular(matrix):
        return None
    cols = len(matrix[0])
    sums = [0] * cols
    for row in matrix:
        for j in range(cols):
            sums[j] += row[j]
    return sums


def max_in_matrix(matrix):
    m = None
    for row in matrix:
        for v in row:
            if m is None or v > m:
                m = v
    return m


if __name__ == "__main__":
    print("Téglalap?", is_rectangular(matrix))
    print("Sorösszegek:", row_sums(matrix))
    print("Oszlopösszegek:", col_sums(matrix))
    print("Max:", max_in_matrix(matrix))
    print("Rossz mátrix col_sums:", col_sums([[1, 2], [3]]))
