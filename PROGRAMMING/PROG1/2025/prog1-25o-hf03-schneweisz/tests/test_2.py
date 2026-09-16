import random
import string

import hf2_titkosiras as hf2


def test_caesar():
    for i in range(27):
        length = random.randint(1, 20)
        text = ''.join(random.choices(string.printable, k=length))
        result = hf2.caesar_cipher(text, i)
        assert isinstance(result, str)
        assert len(result) == length
