"""
Implementáld az alábbi függvényeket!
"""


def remove_divisors(numbers, multiple):
    """A kapott listából kitörli a multiple paraméterben megadott szám osztóit,
        és visszaadja őket egy új listában.
    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> remove_divisors(numbers, 30)
    [1, 2, 3, 5, 6]
    >>> numbers
    [4, 7, 8, 9]
    """
    removed = []
    
    i = 0
    while i < len(numbers):
        if multiple % numbers[i] == 0:
            removed.append(numbers[i])
            numbers.pop(i)
        else:
            i += 1

    return removed


def prime_factors(number):
    """Visszaadja a kapott szám prímtényezőinek listáját.
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(24)
    [2, 2, 2, 3]
    >>> prime_factors(1)
    []
    >>> prime_factors(2)
    [2]
    >>> prime_factors(3)
    [3]
    """
    factors= []

    while number % 2 == 0:
        factors.append(2)
        number //= 2
    i = 3

    while i * i <= number:
        while number % i == 0:
            factors.append(i)
            number //= i
        i += 2

    if number > 1:
        factors.append(number)

    return factors


def nontrivial_divisors(number):
    """Visszaadja a kapott szám valódi osztóit (ami nem önmaga vagy 1).
    >>> nontrivial_divisors(12)
    [2, 3, 4, 6]
    >>> nontrivial_divisors(24)
    [2, 3, 4, 6, 8, 12]
    >>> nontrivial_divisors(1)
    []
    >>> nontrivial_divisors(2)
    []
    >>> nontrivial_divisors(3)
    []
    >>> nontrivial_divisors(4)
    [2]
    """
    divisors = []
    
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)  
    return divisors

def common_divisors(numbers):
    """Visszaadja a kapott számok közös osztóinak listáját.
    >>> common_divisors([12, 24])
    [1, 2, 3, 4, 6, 12]
    >>> common_divisors([15, 24])
    [1, 3]
    >>> common_divisors([60, 120, 16, 20])
    [1, 2, 4]
    """
    min_number = min(numbers)
    com_div_l = []

    for i in range(1, min_number+1):
        is_common_divisor = True
        for num in numbers:
            if num % i != 0:
                is_common_divisor = False
                break
        if is_common_divisor:
            com_div_l.append(i)
        
    return com_div_l



if __name__ == "__main__":
    import doctest
    doctest.testmod()
