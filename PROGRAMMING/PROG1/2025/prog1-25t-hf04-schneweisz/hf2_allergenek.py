"""
Implementáld az alábbi függvényeket!
"""

allergenek = ["glutén", "tej", "mogyoró", "tojás", "hal", "rákfélék", "szója"]


def collect_allergenes(menu: dict[str, list[int]]) -> dict[str, list[str]]:
    """Összegyűjti, hogy mely allergének mely ételekben szerepelnek.

    Kap egy dictet, melyben a kulcsok az ételek nevei, az értékek pedig a benne található allergének indexeinek listái.
    Az indexek a fenti `allergenek` listának megfelelően vannak megadva.

    Visszaad egy dictet, melyben a kulcsok az allergének nevei, az értékek pedig az ételek listái, melyekben előfordulnak.
    Csak olyan allergének szerepeljenek a visszaadott dictben, melyek valamilyen ételben előfordulnak!

    >>> collect_allergenes({"tészta": [0, 3], "krumplipüré": [0, 1, 3], "halászlé": [4, 5], "húsleves": []}) \
        == {'glutén': ['tészta', 'krumplipüré'], 'tej': ['krumplipüré'], 'tojás': ['tészta', 'krumplipüré'], 'hal': ['halászlé'], 'rákfélék': ['halászlé']}
    True
    """
    allergenes = {}
    for key, value in menu.items():
        for item in value:
            if allergenek[item] not in allergenes:
                allergenes[allergenek[item]] = []
                allergenes[allergenek[item]].append(key)
            else:
                allergenes[allergenek[item]].append(key)
    return allergenes


def filter_menu(menu: dict[str, list[int]], allergenes: list[str]) -> list[str]:
    """ Szűri az étlapot egy megadott allergénlista alapján.

    Kap egy olyan dictet, mint a collect_allergenes, valamint egy listát egy vendég allergéneinek neveivel.
    Visszaad egy listát, melyben azon ételek szerepelnek a menüről, melyekben nincs benne az allergének közül egy sem.
    Az eredménylistában az ételek sorrendje megegyezik a menüben lévő sorrenddel.

    >>> filter_menu({"tészta": [0, 3], "krumplipüré": [0, 1, 3], "halászlé": [4, 5], "húsleves": []}, ["glutén", "tej"])
    ['halászlé', 'húsleves']
    """
    collected = collect_allergenes(menu)
    filtered_menu = []
    to_filter = set()

    for key, value in collected.items():
        if key in allergenes:
            for meal in value:
                to_filter.add(meal)
    
    for elem in menu.keys():
        if elem not in to_filter:
            filtered_menu.append(elem)
       
    return filtered_menu
