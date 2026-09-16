import random
from copy import deepcopy

from pytest import approx

import hf0_tavolsagok as hf0


def test_distance():
    for count in range(2, 20):
        x = [random.randint(-10, 10) for _ in range(count)]
        y = [random.randint(-10, 10) for _ in range(count)]
        names = [chr(ord("A") + i) for i in range(count)]
        random.shuffle(names)
        places = [{"name": names[i], "x": x[i], "y": y[i]} for i in range(count)]
        before = deepcopy(places)
        for _ in range(count // 2):
            start, end = random.sample(range(count), 2)
            result = hf0.distance(places, names[start], names[end])
            assert (
                places == before
            ), f"Változott a lista: {before} -> distance(places, {start}, {end}) -> {places}"
            assert result**2 == approx(
                (x[start] - x[end]) ** 2 + (y[start] - y[end]) ** 2
            ), f"Rossz érték: {before} -> distance(places, {names[start]}, {names[end]}) -> {result}"
