"""
Az alábbi globális változóban lévő dict fogja tárolni a hallgatók órai aktivitását.
Implementáld a függvényeket, melyekkel módosíthatók és lekérdezhetők az aktivitások!
"""

aktivitas = dict[str, int]()


def add_activity(name: str) -> None:
    """Növeli a megadott hallgató aktivitását eggyel.

    Ha még nem szerepel a hallgató a dictionaryben, akkor bekerül.

    >>> akitivitas = dict[str, int]()
    >>> add_activity("Béla")
    >>> aktivitas
    {'Béla': 1}
    >>> add_activity("Béla")
    >>> aktivitas
    {'Béla': 2}
    >>> add_activity("Feri")
    >>> aktivitas
    {'Béla': 2, 'Feri': 1}
    >>> add_activity("Lilla")
    >>> add_activity("Béla")
    >>> add_activity("Lilla")
    >>> aktivitas
    {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    """
    if name in aktivitas:
        aktivitas[name] += 1
    else:
        aktivitas[name] = 1


def get_activity(name: str) -> int:
    """Visszaadja a megadott hallgató aktivitását.

    Ha a hallgató nem szerepel a dictionaryben, akkor 0-t ad vissza.

    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> get_activity("Béla")
    3
    >>> get_activity("Feri")
    1
    >>> get_activity("Anna")
    0
    """
    if name in aktivitas:
        return aktivitas[name]
    else:
        return 0


def get_most_active() -> str:
    """Visszaadja a legaktívabb hallgató nevét.

    Ha több hallgató is ugyanannyi aktivitással rendelkezik, akkor bármelyiket.
    Ha nincs hallgató, akkor adjon vissza üres stringet.

    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> get_most_active()
    'Béla'
    """
    max_name = ''
    max_value = -1

    for name, value in aktivitas.items():
        if value > max_value:
            max_name = name
            max_value = value
    return max_name


def get_least_active() -> str:
    """Visszaadja a legkevésbé aktív hallgató nevét.

    Ha több hallgató is ugyanannyi aktivitással rendelkezik, akkor bármelyiket.
    Ha nincs hallgató, akkor adjon vissza üres stringet.

    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> get_least_active()
    'Feri'
    """
    min_name = ''
    min_value = aktivitas[get_most_active()]

    for name, value in aktivitas.items():
        if name not in aktivitas:
            return ''
        if value < min_value:
            min_name = name
            min_value = value
    return min_name


def total_activity() -> int:
    """Visszaadja az összes hallgatói aktivitás összegét.

    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> total_activity()
    6
    """
    
    return sum(aktivitas.values())
