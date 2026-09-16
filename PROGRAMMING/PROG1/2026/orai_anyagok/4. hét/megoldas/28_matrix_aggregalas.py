matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def is_rectangular(matrix):
    if len(matrix)==0:
        return True
    width=len(matrix[0])
    for row in matrix:
        if len(row)!=width:
            return False
    return True

def col_sums(matrix):
    if len(matrix)==0:
        return []
    if not is_rectangular(matrix):
        return None
    
    cols=len(matrix[0])
    out=[0]*cols
    for row in matrix:
        for i in range(cols):
            out[i]+=row[i]
    return out
if __name__ == "__main__":
    print(col_sums(matrix))