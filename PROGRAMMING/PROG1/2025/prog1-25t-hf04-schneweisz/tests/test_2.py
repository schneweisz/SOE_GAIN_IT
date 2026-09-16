import random

from pytest import fail

import hf2_allergenek as hf2

dishes = {
    "tészta": [0, 3],
    "krumplipüré": [0, 1, 3],
    "halászlé": [4, 5],
    "krumplisaláta": [0, 1, 3],
    "csokitorta": [0, 1, 2],
    "húsleves": [],
    "miso leves": [6],
    "sushi": [4, 5, 6],
}


def test_collect_allergenes():
    for _ in range(10):
        count = random.randrange(1, len(dishes))
        menu = {d: a for d, a in random.sample(list(dishes.items()), count)}
        before = menu.copy()
        result = hf2.collect_allergenes(menu)
        assert menu == before, f"Az eredeti dictionary megváltozott: {menu} -> {result}"
        assert isinstance(
            result, dict
        ), f"Hibás a visszatérési érték: {menu} -> {result}"
        for dish, allergenes in menu.items():
            for allergene in allergenes:
                assert (
                    dish in result[hf2.allergenek[allergene]]
                ), f"{dish} hiányzik {hf2.allergenek[allergene]} listájából: {menu} -> {result}"
        for allergene, meals in result.items():
            assert len(meals) > 0, f"{allergene} listája üres: {menu} -> {result}"
            for dish in meals:
                assert (
                    dish in menu
                ), f"{dish} nem szerepel az étlapon: {menu} -> {result}"
                assert (
                    hf2.allergenek.index(allergene) in menu[dish]
                ), f"{dish} nem tartalmaz {allergene} allergént: {menu} -> {result}"


def test_filter_menu():
    for _ in range(10):
        count = random.randrange(1, len(dishes))
        menu = {d: a for d, a in random.sample(list(dishes.items()), count)}
        allergenes = random.sample(
            hf2.allergenek, random.randrange(1, len(hf2.allergenek))
        )
        before = menu.copy()
        result = hf2.filter_menu(menu, allergenes)
        assert menu == before, f"Az eredeti dictionary megváltozott: {menu} -> {result}"
        assert isinstance(
            result, list
        ), f"Hibás a visszatérési érték: {menu}, {allergenes} -> {result}"
        for dish in result:
            assert (
                dish in menu
            ), f"{dish} nem szerepel az étlapon: {menu}, {allergenes} -> {result}"
            for allergene in allergenes:
                assert (
                    hf2.allergenek.index(allergene) not in menu[dish]
                ), f"{dish} tartalmaz {allergene} allergént: {menu}, {allergenes} -> {result}"
        for dish, ingredients in menu.items():
            if dish not in result:
                for allergene in allergenes:
                    if hf2.allergenek.index(allergene) in ingredients:
                        break
                else:
                    fail(
                        f"{dish} nem szerepel a szűrt listában: {menu}, {allergenes} -> {result}"
                    )
