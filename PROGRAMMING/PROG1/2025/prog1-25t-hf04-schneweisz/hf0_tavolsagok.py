"""Implementálni kell az alábbi függvényt."""

from typing import Any


def distance(places: list[dict[str, Any]], start: str, end: str) -> float:
    """Kiszámolja két nevesített hely légvonalbeli távolságát.

    Args:
        places (list[dict[str, Any]]): Helyek adatai, a dictek kulcsai: name, x, y
        start (str): Indulási hely neve
        end (str): Végpont neve

    Returns:
        float: Légvonalbeli távolság

    >>> distance([{"name": "A", "x": 0, "y": 0}, {"name": "B", "x": 1, "y": 0}, {"name": "C", "x": 1, "y": 1}], "A", "C")
    1.4142135623730951
    """
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    for elem in places:
        if elem["name"] == start:
            start_x = elem["x"]
            start_y = elem["y"]
        if elem["name"] == end:
            end_x = elem["x"]
            end_y = elem["y"]
    dx = end_x - start_x
    dy = end_y - start_y
    return (dx ** 2 + dy ** 2) ** 0.5

result = distance([{"name": "A", "x": 0, "y": 0}, {"name": "B", "x": 1, "y": 0}, {"name": "C", "x": 1, "y": 1}], "A", "C")

print(result)
    