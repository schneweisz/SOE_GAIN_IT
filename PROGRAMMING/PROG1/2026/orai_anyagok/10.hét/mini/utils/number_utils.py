def is_even(n):
    """Eldönti, hogy a szám páros-e

    Args:
        n: Vizsgált szám.
    
    Returns:
        'True', ha a szám páros, különben 'False'

    Examples:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
    """
    return n%2==0

def is_positive(n):
    """Eldönti, hogy a szám páros-e

    Args:
        n: Vizsgált szám.
    
    Returns:
        'True', ha a nagyobb mint 0, különben 'False'

    Examples:
        >>> is_positive(4)
        True
        >>> is_positive(0)
        False
    """
    return n>0

def absolute_value(n):
    """Visszaadja a szám abszolútértékét

    Args:
        n: Vizsgált szám.
    
    Returns:
        A szám abszolútértéke

    Examples:
        >>> absolute_value(4)
        4
        >>> absolute_value(-5)
        5
    """
    if n<0:
        return -n
    return n

def square(n):
    """Visszaadja a szám négyzetét

    Args:
        n: Vizsgált szám.
    
    Returns:
        A szám négyzete

    Examples:
        >>> square(5)
        25
        >>> square(2)
        4
    """
    return n*n

def cube(n):
    """Visszaadja a szám köbét

    Args:
        n: Vizsgált szám.
    
    Returns:
        A szám négyzete

    Examples:
        >>> cube(4)
        64
        >>> cube(-2)
        -8
    """
    return n*n*n
#python -m pip install numpy
#python3 -m pip install numpy

#python -m pip install ipython
#python3 -m pip install ipython