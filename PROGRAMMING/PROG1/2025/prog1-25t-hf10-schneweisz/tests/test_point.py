import math
import random

from point import Point

def test_point():
    p = Point()
    assert (p.x, p.y) == (0, 0)
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    r = Point(x, y)
    assert (r.x, r.y) == (x, y)

def test_distance():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    a = Point(x, y)
    b = Point(x, y)
    assert a.distance(b) == 0
    alpha = random.uniform(0, 2 * math.pi)
    dist = random.uniform(0.1, 5)
    dx = dist * math.sin(alpha)
    dy = dist * math.cos(alpha)
    b = Point(x + dx, y + dy)
    assert math.isclose(a.distance(b), dist, rel_tol=1e-3)

def test_eq():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    a = Point(x, y)
    b = Point(x, y)
    assert a == b
    for d in range(-5, 5):
        if d == 0:
            continue
        b = Point(x + d, y)
        assert a != b
        assert b != a
        b = Point(x, y + d)
        assert a != b
        assert b != a
        b = Point(x + d, y + d)
        assert a != b
        assert b != a

def test_str():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    a = Point(x, y)
    s = str(a)
    assert str(x) in s
    assert str(y) in s
    assert "," in s
    assert s[0] == "("
    assert s[-1] == ")"

def test_repr():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    a = Point(x, y)
    s = f"{a!r}"
    assert str(x) in s
    assert str(y) in s
    assert "," in s
    assert s.startswith("Point(")
    assert s[-1] == ")"
