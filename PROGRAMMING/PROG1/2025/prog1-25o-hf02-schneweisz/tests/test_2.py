import random

import hf2_oszthatosag as hf2


def test_remove_divisors():
    for _ in range(42):
        length = random.randint(1, 20)
        numbers = [random.randint(1, 10) for _ in range(length)]
        multiple = random.randint(1, 60)
        divisors = hf2.remove_divisors(numbers, multiple)
        assert isinstance(divisors, list)
        for d in divisors:
            assert isinstance(d, int)
            assert multiple % d == 0
        for n in numbers:
            assert multiple % n != 0


def test_prime_factors():
    for _ in range(42):
        number = random.randint(1, 1000)
        factors = hf2.prime_factors(number)
        assert isinstance(factors, list)
        product = 1
        for f in factors:
            assert isinstance(f, int)
            assert number % f == 0
            assert f != 1, "1 is not a prime number"
            for i in range(2, int(f**0.5) + 1):
                assert f % i != 0, f"{f} is not a prime number"
            product *= f
        assert product == number


def test_nontrivial_divisors():
    for _ in range(42):
        number = random.randint(1, 1000)
        divisors = hf2.nontrivial_divisors(number)
        assert isinstance(divisors, list)
        for d in divisors:
            assert isinstance(d, int)
            assert number % d == 0
            assert d != 1, f"1 is not a nontrivial divisor of {number}"
            assert d != number, f"{number} is not a divisor of itself"
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                assert i in divisors
                assert number // i in divisors


def test_common_divisors():
    for _ in range(100):
        length = random.randint(1, 5)
        numbers = [random.randint(100, 200) for _ in range(length)]
        divisors = hf2.common_divisors(numbers)
        assert isinstance(divisors, list)
        for d in divisors:
            assert isinstance(d, int)
            for n in numbers:
                assert n % d == 0
        assert 1 in divisors
        for i in range(2, min(numbers) + 1):
            if all(n % i == 0 for n in numbers):
                assert i in divisors
