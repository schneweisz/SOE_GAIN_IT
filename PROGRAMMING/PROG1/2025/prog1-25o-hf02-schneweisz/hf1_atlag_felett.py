"""
Implementáld az alábbi függvényeket!
"""

def average(numbers):
    """Visszaadja a kapott listában lévő számok átlagát.
    >>> average([1, 2, 3, 4])
    2.5
    >>> average([1, 2, 3, 4, 5])
    3.0
    """
    sum = 0
    for i in range (len(numbers)):
        sum += numbers[i]
        avg = sum/len(numbers)
    return avg


def count_greater_than(numbers, threshold):
    """Visszaadja, hogy a számokból hány nagyobb a megadott küszöbértéknél.
    >>> count_greater_than([1, 2, 3, 4], 2)
    2
    """
    db = 0
    for i in range (len(numbers)):
        if numbers[i] > threshold:
            db += 1
    return db


# A megoldás során használd fel a fent megírt függvényeket!
def count_greater_than_average(numbers):
    """Visszaadja, hogy a számokból hány nagyobb az átlagnál.
    >>> count_greater_than_average([1, 2, 3, 4])
    2
    """

    return count_greater_than(numbers, average(numbers))
    


# A megoldás során használd fel a fenti average függvényt!
def delete_lower_than_average(numbers):
    """Kitörli a listából az átlag alattiakat.
    >>> numbers = [1, 2, 3, 4]
    >>> delete_lower_than_average(numbers)
    >>> numbers
    [3, 4]
    """
    avg = average(numbers)
    i = 0
    while i < len(numbers):
        if numbers[i] < avg:
            del numbers[i]
        else:
            i += 1
    pass


if __name__ == "__main__":
    # Doctestek futtatása scriptből:
    import doctest
    doctest.testmod()
    # Parancssorból: python -m doctest [-v] <filename>
    # Pytest-tel: pytest --doctest-modules [-k <filename>]
