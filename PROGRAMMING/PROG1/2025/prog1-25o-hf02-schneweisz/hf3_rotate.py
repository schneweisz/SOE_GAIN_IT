"""
Implementáld az alábbi függvényeket!
"""


def shift(values):
    """Elcsúsztatja a kapott values lista elemeit 1 hellyel jobbra.
    Az utolsó elem az elejére kerül.
    >>> values = [1, 2, 3, 4]
    >>> shift(values)
    >>> values
    [4, 1, 2, 3]
    >>> shift(values)
    >>> values
    [3, 4, 1, 2]
    >>> values = [2]
    >>> shift(values)
    >>> values
    [2]
    >>> values = []
    >>> shift(values)
    >>> values
    []
    """
    for i in range(len(values)-1, 0, -1):
        seged = values[i]
        values[i] = values[i-1]
        values[i-1] = seged
    pass


def shifted(values):
    """Visszaadja a kapott values lista elcsúsztatott változatát.
    Az eredmény egy olyan lista, ahol minden elem 1 hellyel jobbra kerül,
    az utolsót kivéve, ami az elejére kerül.
    >>> shifted([1, 2, 3, 4])
    [4, 1, 2, 3]
    >>> shifted([5, 4, 3, 2, 1])
    [1, 5, 4, 3, 2]
    >>> shifted([2])
    [2]
    >>> shifted([])
    []
    """
    shifted = []
    temp = values[:]
    shift(temp)
    shifted.extend(temp)
    return shifted


def rotate(values, shift_by):
    """Elforgatja a kapott values lista elemeit shift_by hellyel jobbra.
    Az utolsó shift_by elem az elejére kerül.
    Negatív shift_by esetén balra mozdulnak el az elemek.
    >>> values = [1, 2, 3, 4, 5]
    >>> rotate(values, 2)
    >>> values
    [4, 5, 1, 2, 3]
    >>> rotate(values, -2)
    >>> values
    [1, 2, 3, 4, 5]
    >>> rotate(values, 0)
    >>> values
    [1, 2, 3, 4, 5]
    >>> rotate(values, 6)
    >>> values
    [5, 1, 2, 3, 4]
    """
    if shift_by > len(values):
        shift_by = shift_by - len(values)

    if shift_by > 0:
        for shift in range(shift_by):
            for i in range(len(values)-1, 0, -1):
                seged = values[i]
                values[i] = values[i-1]
                values[i-1] = seged
    elif shift_by < 0:
        shift_by -= shift_by*2
        for shift in range(shift_by):
            for i in range(len(values)-1):
                seged = values[i]
                values[i] = values[i+1]
                values[i+1] = seged
    pass


def rotated(values, shift_by):
    """Visszaadja a kapott values lista "elforgatott" mását.
    Az elforgatás során minden elem shift_by hellyel jobbra kerül,
    az utolsó index után az elején folytatva a sort.
    Negatív shift_by esetén balra mozdulnak el az elemek.
    >>> rotated([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> rotated([1, 2, 3, 4, 5], -2)
    [3, 4, 5, 1, 2]
    >>> rotated([1, 2, 3, 4, 5], 0)
    [1, 2, 3, 4, 5]
    >>> rotated([1, 2, 3, 4, 5], 5)
    [1, 2, 3, 4, 5]
    >>> rotated([1, 2, 3, 4, 5], 51)
    [5, 1, 2, 3, 4]
    """
    rotated_list = []
    temp = values[:]
    rotate(temp, shift_by)
    rotated_list.extend(temp)   

    return rotated_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
