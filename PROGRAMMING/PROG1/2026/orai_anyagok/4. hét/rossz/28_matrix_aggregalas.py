matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8],
]


def col_sums_rosszul(matrix):
    #feltétezeli hogy minden sor ugyanannyi hoszú 
    cols = len(matrix[0])
    out = [0] * cols
    for row in matrix:
        for j in range(cols):
            out[j] += row[j] #index error lehet
    return out

 
if __name__ == "__main__":
    print(col_sums_rosszul(matrix))
