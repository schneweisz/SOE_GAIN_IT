from io import StringIO
from unittest.mock import patch

from hallgato import select_hallgato


def test_select_hallgato():
    cases = {
        "1": "MNO345",
        "2": "STU901",
        "3": "ABC123",
        "4": "DEF456",
        "5": "GHI789",
        "6": "PQR678",
        "7": "JKL012",
    }
    for inp, out in cases.items():
        with patch("sys.stdout", StringIO()) as fake_out:
            with patch("builtins.input", return_value=inp):
                neptun = select_hallgato()
                output = fake_out.getvalue().strip()
        expected_out = """Hallgatók:
1: Horváth Milán (MNO345)
2: Király István (STU901)
3: Kiss Ádám (ABC123)
4: Kovács Dávid (DEF456)
5: Nagy Gréta (GHI789)
6: Papp Réka (PQR678)
7: Tóth Júlia (JKL012)
Adja meg a hallgató sorszámát:"""
        for line, expected_line in zip(output.split("\n"), expected_out.split("\n")):
            assert line.strip() == expected_line.strip()
        assert neptun == out, f"input = {inp}"
