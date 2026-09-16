import random
import hf3_rotate as hf3


def test_shift():
    for length in range(42):
        values = [random.randint(0, 10) for _ in range(length)]
        original = values.copy()
        hf3.shift(values)
        assert len(values) == length, "Nem marad ugyanolyan hosszú a lista!"
        if length:
            assert values == [original[-1]] + original[:-1]


def test_shifted():
    for length in range(42):
        values = [random.randint(0, 10) for _ in range(length)]
        original = values.copy()
        result = hf3.shifted(values)
        assert isinstance(result, list), "Nem listát ad vissza!"
        assert original == values, "Módosult az eredeti lista!"
        assert len(result) == length, "Nem ugyanolyan hosszú listát ad vissza!"
        if length:
            assert result == [values[-1]] + values[:-1]


def test_rotate():
    for length in range(42):
        values = [random.randint(0, 10) for _ in range(length)]
        original = values.copy()
        hf3.rotate(values, 0)
        assert values == original, "Módosult az eredeti lista!"
        shift_by = random.randrange(-2 * (length + 2), 2 * (length + 2))
        hf3.rotate(values, shift_by)
        assert len(values) == length, "Nem marad ugyanolyan hosszú a lista!"
        if length:
            x = shift_by % length
            assert values == original[-x:] + original[:-x]


def test_rotated():
    for length in range(0, 10):
        values = [random.randint(0, 10) for _ in range(length)]
        original = values.copy()
        result = hf3.rotated([], length)
        assert result == [], "Nem üres listát ad vissza!"
        result = hf3.rotated([], -length)
        assert result == [], "Nem üres listát ad vissza!"
        for shift_by in range(-2 * (length + 2), 2 * (length + 2)):
            result = hf3.rotated(values, shift_by)
            assert isinstance(result, list), "Nem listát ad vissza!"
            assert original == values, "Módosult az eredeti lista!"
            assert len(result) == length, "Nem ugyanolyan hosszú listát ad vissza!"
            if length:
                x = shift_by % length
                assert result == values[-x:] + values[:-x]
