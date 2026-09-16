"""
Implementáld az alábbi függvényeket!
"""

import doctest


def convert_to_base(number, base):
    """Visszaadja a kapott egész számot base-alapú számrendszerben írt stringként.
    10-nél nagyobb számrendszer esetén a 9-est követő számjegyek ABCDEFG...
    A base 2 és 36 közötti egész szám lehet.
    >>> convert_to_base(5, 2)
    '101'
    >>> convert_to_base(136, 8)
    '210'
    >>> convert_to_base(1100, 16)
    '44C'
    """
    result = ""
    if number == 0:
        result = "0"
    while number > 0:
        maradek = number % base
        number //= base
        if maradek < 10:
            result += str(maradek)        
        else:
            result += chr(ord('A') + maradek - 10)

    return result[::-1]



if __name__ == "__main__":
    doctest.testmod()
