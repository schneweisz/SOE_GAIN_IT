import random
from unittest.mock import patch

from pytest import approx

import hf1_atlag_felett as hf1


def test_average():
    for _ in range(42):
        count = random.randint(1, 20)
        avg = random.uniform(0, 100)
        numbers = [avg for _ in range(count)]
        if count > 1:
            for _ in range(int(count**1.5)):
                i, j = random.sample(range(count), 2)
                d = random.uniform(-10, 10)
                numbers[i] += d
                numbers[j] -= d
        result = hf1.average(numbers)
        assert result == approx(avg)


def test_count_greater_than():
    for _ in range(42):
        length = random.randint(1, 10)
        count = random.randint(0, length)
        threshold = random.randint(30, 70)
        numbers = [random.randint(0, threshold) for _ in range(length - count)]
        numbers += [random.randint(threshold + 1, 100) for _ in range(count)]
        random.shuffle(numbers)
        result = hf1.count_greater_than(numbers, threshold)
        assert result == count


def test_count_greater_than_average():
    for _ in range(33):
        length = random.randint(1, 10)
        numbers = [random.randint(0, 10) for _ in range(length)]
        with patch(
            "hf1_atlag_felett.count_greater_than",
            side_effect=hf1.count_greater_than,
        ) as mock_count_greater_than:
            with patch(
                "hf1_atlag_felett.average", side_effect=hf1.average
            ) as mock_average:
                result = hf1.count_greater_than_average(numbers)
                assert isinstance(result, int)
                mock_average.assert_called_once_with(numbers)
            avg = sum(numbers) / length
            assert isinstance(avg, float) or isinstance(avg, int)
            mock_count_greater_than.assert_called_once_with(numbers, avg)
        sorted_numbers = sorted(numbers, reverse=True)
        if result > 0:
            assert sorted_numbers[result - 1] > avg
        assert sorted_numbers[result] <= avg


def test_delete_lower_than_average():
    for _ in range(33):
        length = random.randint(1, 10)
        numbers = [random.randint(0, 10) for _ in range(length)]
        original_numbers = numbers.copy()
        avg = sum(numbers) / length
        with patch(
            "hf1_atlag_felett.average", side_effect=hf1.average
        ) as mock_average:
            hf1.delete_lower_than_average(numbers)
            assert isinstance(avg, float) or isinstance(avg, int)
            mock_average.assert_called_once_with(numbers)
        for number in numbers:
            assert number >= avg
            assert number in original_numbers
        for number in original_numbers:
            if number < avg:
                assert number not in numbers
            else:
                assert number in numbers
