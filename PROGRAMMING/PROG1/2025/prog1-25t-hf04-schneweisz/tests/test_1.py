import random

import hf1_aktivitas_szamlalo as hf1

names = [
    "Béla",
    "Lilla",
    "Feri",
    "Józsi",
    "Kati",
    "Géza",
    "Károly",
    "Éva",
    "Péter",
    "Judit",
    "Ádám",
    "Hanna",
    "Márk",
    "Mónika",
    "Zsuzsa",
]


def test_add_activity():
    for _ in range(10):
        hf1.aktivitas.clear()
        for _ in range(random.randint(1, 100)):
            before = hf1.aktivitas.copy()
            name = random.choice(names)
            hf1.add_activity(name)
            assert (
                name in hf1.aktivitas
            ), f"Nem került be {name}: {before} -> add_activity({name}) -> {hf1.aktivitas}"
            assert (
                hf1.aktivitas[name] == before.get(name, 0) + 1
            ), f"Nem nőtt az érték: {before} -> add_activity({name}) -> {hf1.aktivitas}"
            for other in names:
                if other == name:
                    continue
                if other in before:
                    assert (
                        other in hf1.aktivitas
                    ), f"Elveszett {other}: {before} -> add_activity({name}) -> {hf1.aktivitas}"
                    assert (
                        hf1.aktivitas[other] == before[other]
                    ), f"Változott {other} értéke: {before} -> add_activity({name}) -> {hf1.aktivitas}"
                else:
                    assert (
                        other not in hf1.aktivitas
                    ), f"Bekerült {other}: {before} -> add_activity({name}) -> {hf1.aktivitas}"


def test_get_activity():
    for _ in range(10):
        count = random.randrange(1, len(names))
        hf1.aktivitas = {
            name: random.randint(1, 100) for name in random.sample(names, count)
        }
        before = hf1.aktivitas.copy()
        for name in names:
            got = hf1.get_activity(name)
            if name in before:
                assert (
                    got == before[name]
                ), f"Rossz érték: {before} -> get_activity({name}) -> {hf1.get_activity(name)}"
            else:
                assert (
                    got == 0
                ), f"Rossz érték: {before} -> get_activity({name}) -> {hf1.get_activity(name)}"
            assert (
                before == hf1.aktivitas
            ), f"Változott a dict: {before} -> get_activity({name}) -> {hf1.aktivitas}"


def test_get_most_active():
    for _ in range(10):
        count = random.randrange(1, len(names))
        hf1.aktivitas = {
            name: random.randint(1, 100) for name in random.sample(names, count)
        }
        before = hf1.aktivitas.copy()
        result = hf1.get_most_active()
        assert (
            hf1.aktivitas == before
        ), f"Változott a dict: {before} -> get_most_active() -> {hf1.aktivitas}"
        assert (
            result in hf1.aktivitas
        ), f"Nincs ilyen név: {before} -> get_most_active() -> {hf1.get_most_active()}"
        for name, val in hf1.aktivitas.items():
            assert before[result] >= val, f"{name} aktívabb mint {result}: {before}"


def test_get_least_active():
    for _ in range(10):
        count = random.randrange(1, len(names))
        hf1.aktivitas = {
            name: random.randint(1, 100) for name in random.sample(names, count)
        }
        before = hf1.aktivitas.copy()
        result = hf1.get_least_active()
        assert (
            hf1.aktivitas == before
        ), f"Változott a dict: {before} -> get_least_active() -> {hf1.aktivitas}"
        assert (
            result in hf1.aktivitas
        ), f"Nincs ilyen név: {before} -> get_least_active() -> {hf1.get_least_active()}"
        for name, val in hf1.aktivitas.items():
            assert before[result] <= val, f"{name} passzívabb mint {result}: {before}"


def test_total_activity():
    for _ in range(10):
        hf1.aktivitas = {}
        for i in range(100):
            before = hf1.aktivitas.copy()
            result = hf1.total_activity()
            assert (
                hf1.aktivitas == before
            ), f"Változott a dict: {before} -> total_activity() -> {hf1.aktivitas}"
            assert (
                result == i
            ), f"Rossz összeg: {before} -> total_activity() -> {result}"
            name = random.choice(names)
            hf1.add_activity(name)
