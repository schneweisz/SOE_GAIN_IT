"""Feladat: javítsd úgy, hogy a mátrix kiértékelés működjön.

Elvárt:
- is_rectangular: True/False
- row_sums, col_sums: helyes összegek
- max_in_matrix: maximum elem (üres mátrixnál None)
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


def is_rectangular(matrix):
    # hiba: csak az első két sort hasonlítja
    if len(matrix) == 0:
        return True
    return len(matrix[0]) == len(matrix[1])


def row_sums(matrix):
    # hiba: a s változó nincs lenullázva soronként
    sums = []
    s = 0
    for row in matrix:
        for v in row:
            s += v
        sums.append(s)
    return sums


def col_sums(matrix):
    # hiba: feltételezi, hogy téglalap, és rossz indexelés
    cols = len(matrix)
    sums = [0] * cols
    for row in matrix:
        for j in range(cols):
            sums[j] += row[j]
    return sums


def max_in_matrix(matrix):
    # hiba: rossz kezdőérték (0), negatívaknál rossz
    m = 0
    for row in matrix:
        for v in row:
            if v > m:
                m = v
    return m


if __name__ == "__main__":
    print("Téglalap?", is_rectangular(matrix))
    print("Sorösszegek:", row_sums(matrix))
    print("Oszlopösszegek:", col_sums(matrix))
    print("Max:", max_in_matrix(matrix))
