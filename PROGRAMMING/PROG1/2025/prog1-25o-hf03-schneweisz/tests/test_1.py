import random

import hf1_szamrendszer as hf1


def test_convert_to_base():
    for i in range(100):
        number = random.randint(0, 20 * i)
        for b in [2, 8, 16] + random.sample(range(3, 37), 10):
            result = hf1.convert_to_base(number, b)
            assert isinstance(result, str)
            assert int(result, b) == number
