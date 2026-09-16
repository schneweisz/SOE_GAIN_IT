"""
Implementáld az alábbi függvényeket, melyek személyek ismeretségi hálózatával dolgoznak.
Készíthetsz további segédfüggvényeket is.
"""

friend_network = dict[str, list[str]]()
"""A kulcsok a személyek nevei, az értékek pedig a személyek barátlistái.
A barátságok kétirányúak, azaz ha A-nak barátja B, akkor B-nek is barátja A.
"""

import json
def add_friendship(name1: str, name2: str) -> None:
    """Hozzáadja a barátságot a hálózathoz.

    Ha a barátság már létezik, akkor nem csinál semmit.
    Senki sem lehet saját maga barátja, így ha name1 == name2, akkor nem csinál semmit.
    A barátságok kétirányúak, azaz ha A-nak barátja B, akkor B-nek is barátja A.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("Adam", "Cheryl")
    >>> friend_network == {"Adam": ["Bob", "Cheryl"], "Bob": ["Adam"], "Cheryl": ["Adam"]}
    True
    """
    if name1 == name2:
        return
    if name1 not in friend_network:
        friend_network[name1] = []
    if name2 not in friend_network:
        friend_network[name2] = []

    if name1 not in friend_network[name2]:
        friend_network[name2].append(name1)
    if name2 not in friend_network[name1]:
        friend_network[name1].append(name2)


def are_friends(name1: str, name2: str) -> bool:
    """Megadja, hogy két személy barát-e.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("Adam", "Cheryl")
    >>> are_friends("Adam", "Bob")
    True
    >>> are_friends("Cheryl", "Adam")
    True
    >>> are_friends("Bob", "Cheryl")
    False
    """
    if name2 in friend_network.get(name1, []):
        return True


def common_friends(name1: str, name2: str) -> list[str]:
    """Megadja két személy közös barátait.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("Adam", "Cheryl")
    >>> common_friends("Adam", "Bob")
    []
    >>> common_friends("Cheryl", "Bob")
    ['Adam']
    >>> common_friends("George", "Victoria")
    []
    """
    friends1 =  set(friend_network.get(name1, []))
    friends2 =  set(friend_network.get(name2, []))
    common = []
    for friend in friends1:
        if friend in friends2:
            common.append(friend)
    return common


def most_popular() -> str:
    """Megadja a legnépszerűbb személyt.

    Feltételezi, hogy a hálózatban legalább egy baráti kapcsolat van.
    Egyezőség esetén bármelyik legnépszerűbb személyt adja vissza.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("David", "Adam")
    >>> add_friendship("Bob", "Cheryl")
    >>> most_popular()
    'Adam'
    """
    maxvalue = 0
    maxname = ''
    for name, friends in friend_network.items():
        if len(friends) > maxvalue:
            maxvalue = len(friends)
            maxname = name
    return maxname


def export_network(filename: str) -> None:
    """Kiírja a hálózatot a megadott JSON fájlba.

    Ha a fájl már létezik, akkor felülírja.
    A helytakarékosság érdekében a fájl minden baráti kapcsolatot csak az egyik fél oldaláról tárol.
    """
    unique_network = {}

    for person, friends in friend_network.items():
        unique_friends = []
        for friend in friends:
            if friend not in unique_network or person not in unique_network[friend]:
                unique_friends.append(friend)
        if unique_friends:
            unique_network[person] = unique_friends

    with open(filename, 'w') as f:
        json.dump(unique_network, f, indent=4)

def import_network(filename: str) -> None:
    """Beolvassa a hálózatot a megadott JSON fájlból.

    Az aktuális hálózatot felülírja.
    A fájl minden baráti kapcsolatot csak az egyik fél oldaláról tárol.

    >>> friend_network.clear()
    >>> import_network("hf4_social_network.json")
    >>> are_friends("Bob", "Frank")
    True
    >>> are_friends("Frank", "Bob")
    True
    """
    with open(filename, "r") as f:
        data = json.load(f)

    for person, friends in data.items():
        if person not in friend_network:
            friend_network[person] = []
        for friend in friends:
            if friend not in friend_network:
                friend_network[friend] = []
            if friend not in friend_network[person]:
                friend_network[person].append(friend)
            if person not in friend_network[friend]:
                friend_network[friend].append(person)
