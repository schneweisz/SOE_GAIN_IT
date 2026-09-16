import random

from point import Point
from path import Path

def test_len():
    p = Path()
    assert len(p) == 0

def test_add():
    p = Path()
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    a = Point(x, y)
    p.add(a)
    assert len(p) == 1
    p.add(Point(x, y))
    assert len(p) == 1
    for i in range(1, 10):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        b = Point(x, y)
        while a == b:
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            b = Point(x, y)
        p.add(b)
        assert len(p) == i + 1
        p.add(Point(x, y))
        assert len(p) == i + 1
        a = b

def test_length():
    p = Path()
    assert p.length() == 0
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    a = Point(x, y)
    p.add(a)
    assert p.length() == 0
    total = 0
    for _ in range(10):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        b = Point(x, y)
        while a == b:
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            b = Point(x, y)
        p.add(b)
        total += a.distance(b)
        assert p.length() == total
        a = b
