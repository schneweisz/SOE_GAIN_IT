"""Programozas 1. - doctest gyakorlat, starter fajl.

Futtatas terminalbol:
python -m doctest -v gyak_doctest_starter.py

Feladat:
- Olvasd el a docstringeket.
- Futtasd a doctesteket.
- Ahol nincs teszt, irj legalabb 3-5 doctestet.
- Ahol hibas a kod, javitsd.
- Ahol pass van, implementald a fuggvenyt.
"""


# 1. blokk: bemelegites, egyszeru numerikus fuggvenyek


def add(a: int, b: int) -> int:
    """Ket egesz szam osszeget adja vissza.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Ket egesz szam kulonbseget adja vissza.

    Ird meg a doctesteket:
    - 5 - 2 eredmenye 3
    - 2 - 5 eredmenye -3
    - 0 - 0 eredmenye 0
    """
    return a - b


def square(n: int) -> int:
    """Visszaadja n negyzetet.

    >>> square(4)
    16
    >>> square(-3)
    9
    >>> square(0)
    0
    """
    return n + n


def rectangle_area(width: float, height: float) -> float:
    """Teglalap teruletet szamolja ki.

    >>> rectangle_area(3, 4)
    12
    >>> rectangle_area(2.5, 4)
    10.0
    """
    return width + height


def circle_area(radius: float) -> float:
    """Kor teruletet kozelito ertekkel szamolja: 3.14 * r * r.

    Ird meg a doctesteket:
    - radius 1 eseten 3.14
    - radius 2 eseten 12.56
    - radius 0 eseten 0.0
    """
    pass


# 2. blokk: logikai fuggvenyek es hatarertekek


def is_even(n: int) -> bool:
    """Eldonti, hogy egy egesz szam paros-e.

    Ird meg a doctesteket:
    - pozitiv paros
    - pozitiv paratlan
    - nulla
    - negativ paros
    """
    return n % 2 == 0


def is_adult(age: int) -> bool:
    """Eldonti, hogy az eletkor alapjan valaki felnott-e.

    >>> is_adult(18)
    True
    >>> is_adult(17)
    False
    >>> is_adult(99)
    True
    """
    return age > 18


def is_between(value: int, minimum: int, maximum: int) -> bool:
    """Eldonti, hogy value minimum es maximum kozott van-e, hatarokkal egyutt.

    Ird meg a doctesteket:
    - kozepen levo ertek
    - minimum ertek
    - maximum ertek
    - tul kicsi ertek
    - tul nagy ertek
    """
    pass


def can_vote(age: int, citizen: bool) -> bool:
    """Szavazhat-e valaki, ha legalabb 18 eves es allampolgar.

    >>> can_vote(18, True)
    True
    >>> can_vote(17, True)
    False
    >>> can_vote(20, False)
    False
    """
    return age >= 18 or citizen


# 3. blokk: osztas, kivetel, tipusossag


def divide(a: float, b: float) -> float:
    """Elosztja az elso szamot a masodikkal.

    >>> divide(4, 2)
    2.0
    >>> divide(5, 2)
    2.5
    >>> divide(4, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b


def safe_divide(a: float, b: float) -> float | None:
    """Elosztja az elso szamot a masodikkal, de 0 oszto eseten None-t ad.

    Ird meg a doctesteket:
    - 6 / 3 eredmenye 2.0
    - 5 / 2 eredmenye 2.5
    - 5 / 0 eredmenye None
    """
    pass


def reciprocal(n: float) -> float:
    """Visszaadja egy szam reciprokat.

    >>> reciprocal(4)
    0.25
    >>> reciprocal(0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return n / 1


# 4. blokk: string muveletek


def greet(name: str) -> str:
    """Udvozlo szoveget keszit.

    >>> greet("Anna")
    'Szia, Anna!'
    >>> greet("")
    'Szia, !'
    """
    return "Szia " + name


def first_character(text: str) -> str:
    """Visszaadja a szoveg elso karakteret.

    >>> first_character("alma")
    'a'
    >>> first_character("")
    Traceback (most recent call last):
    ...
    IndexError: string index out of range
    """
    return text[1]


def last_character(text: str) -> str:
    """Visszaadja a szoveg utolso karakteret.

    Ird meg a doctesteket:
    - "alma" eredmenye "a"
    - "Python" eredmenye "n"
    - ures string eseten IndexError
    """
    pass


def count_vowels(text: str) -> int:
    """Megszamolja az angol maganhangzokat egy szovegben.

    >>> count_vowels("alma")
    2
    >>> count_vowels("Python")
    1
    >>> count_vowels("")
    0
    >>> count_vowels("AEIOU")
    5
    """
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def normalize_name(name: str) -> str:
    """Nev normalizalasa: felesleges szokozok levagasa es cim forma.

    Ird meg a doctesteket:
    - " anna " eredmenye "Anna"
    - "KOVACS BELA" eredmenye "Kovacs Bela"
    - "" eredmenye ""
    """
    pass


def initials(full_name: str) -> str:
    """Monogramositja a nevet.

    >>> initials("Kovacs Bela")
    'K.B.'
    >>> initials("Anna")
    'A.'
    >>> initials("  nagy   eva  ")
    'N.E.'
    """
    parts = full_name.split(" ")
    result = ""
    for part in parts:
        result += part[0].upper() + "."
    return result


def is_palindrome(text: str) -> bool:
    """Eldonti, hogy egy szoveg palindrom-e.

    Ird meg a doctesteket:
    - "radar" True
    - "alma" False
    - "Gorog" True legyen kis/nagybetutol fuggetlenul
    - ures string True
    """
    pass


# 5. blokk: listak


def first_item(items: list[int]) -> int:
    """Visszaadja a lista elso elemet.

    >>> first_item([3, 4, 5])
    3
    >>> first_item([])
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    """
    return items[1]


def sum_numbers(numbers: list[int]) -> int:
    """Osszeadja a lista elemeit.

    Ird meg a doctesteket:
    - [1, 2, 3] eredmenye 6
    - [] eredmenye 0
    - [-1, 1] eredmenye 0
    """
    pass


def average(numbers: list[float]) -> float:
    """Visszaadja a lista atlagat.

    >>> average([2, 4, 6])
    4.0
    >>> average([1, 2])
    1.5
    >>> average([])
    Traceback (most recent call last):
    ...
    ValueError: empty list has no average
    """
    return sum(numbers) / len(numbers)


def maximum(numbers: list[int]) -> int:
    """Visszaadja a lista legnagyobb elemet.

    Ird meg a doctesteket:
    - [1, 5, 2] eredmenye 5
    - [-3, -1, -2] eredmenye -1
    - [7] eredmenye 7
    - ures lista eseten ValueError: empty list has no maximum
    """
    pass


def count_positive(numbers: list[int]) -> int:
    """Megszamolja a pozitiv szamokat.

    >>> count_positive([1, -2, 3, 0])
    2
    >>> count_positive([])
    0
    >>> count_positive([-1, -2])
    0
    """
    count = 0
    for number in numbers:
        if number >= 0:
            count += 1
    return count


def filter_even(numbers: list[int]) -> list[int]:
    """Visszaadja a paros szamokat egy uj listaban.

    Ird meg a doctesteket:
    - [1, 2, 3, 4] eredmenye [2, 4]
    - [] eredmenye []
    - [1, 3] eredmenye []
    - [-2, -1, 0] eredmenye [-2, 0]
    """
    pass


# 6. blokk: osszetettebb gyakorlati fuggvenyek


def clamp(value: int, minimum: int, maximum: int) -> int:
    """A value erteket a minimum es maximum koze szoritja.

    >>> clamp(5, 0, 10)
    5
    >>> clamp(-3, 0, 10)
    0
    >>> clamp(15, 0, 10)
    10
    >>> clamp(0, 0, 10)
    0
    >>> clamp(10, 0, 10)
    10
    """
    pass


def grade_text(point: int) -> str:
    """Pontszam alapjan szoveges ertekelest ad vissza.

    0-49: elegtelen
    50-64: elegseges
    65-79: kozepes
    80-89: jo
    90-100: jeles

    Ird meg a doctesteket a hatarertekekre is.
    """
    pass


def shipping_cost(total: int) -> int:
    """Szallitasi koltseget szamol rendelesei osszeg alapjan.

    Szabaly:
    - 20000 Ft-tol ingyenes
    - 10000 Ft-tol 990 Ft
    - kulonben 1490 Ft

    >>> shipping_cost(20000)
    0
    >>> shipping_cost(10000)
    990
    >>> shipping_cost(9999)
    1490
    """
    if total > 20000:
        return 0
    if total > 10000:
        return 990
    return 1490


def password_strength(password: str) -> str:
    """Egyszeru jelszo erosseg vizsgalat.

    Szabaly:
    - 8 karakternel rovidebb: "gyenge"
    - van benne szam es legalabb 8 karakter: "eros"
    - egyebkent: "kozepes"

    Ird meg a doctesteket:
    - "abc" gyenge
    - "abcdefgh" kozepes
    - "abc12345" eros
    - "12345678" eros
    """
    pass


def format_price(price: int) -> str:
    """Ar formazasa Ft vegzodessel.

    >>> format_price(1200)
    '1200 Ft'
    >>> format_price(0)
    '0 Ft'
    """
    return price + " Ft"


def parse_int(text: str) -> int:
    """Szoveget egesz szamma alakit.

    >>> parse_int("42")
    42
    >>> parse_int(" 7 ")
    7
    >>> parse_int("alma")
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'alma'
    """
    return int(text)


def word_count(text: str) -> int:
    """Megszamolja a szavakat.

    Ird meg a doctesteket:
    - "alma korte" eredmenye 2
    - "" eredmenye 0
    - "  sok   szokoz  " eredmenye 2
    """
    pass


def has_duplicate(items: list[int]) -> bool:
    """Eldonti, hogy van-e ismetlodo elem a listaban.

    >>> has_duplicate([1, 2, 3])
    False
    >>> has_duplicate([1, 2, 1])
    True
    >>> has_duplicate([])
    False
    """
    return len(items) == len(set(items))


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Visszaadja a legkisebb es legnagyobb elemet.

    Ird meg a doctesteket:
    - [3, 1, 5] eredmenye (1, 5)
    - [7] eredmenye (7, 7)
    - ures lista eseten ValueError: empty list has no min/max
    """
    pass


# 7. blokk: tovabbi string es validalasi feladatok


def remove_spaces(text: str) -> str:
    """Eltavolitja az osszes szokozt a szovegbol.

    Ird meg a doctesteket:
    - "a b c" eredmenye "abc"
    - "  alma  korte " eredmenye "almakorte"
    - "" eredmenye ""
    """
    pass


def repeat_text(text: str, count: int) -> str:
    """Megismetli a szoveget count alkalommal.

    >>> repeat_text("ha", 3)
    'hahaha'
    >>> repeat_text("x", 0)
    ''
    >>> repeat_text("", 5)
    ''
    """
    return text + count


def contains_digit(text: str) -> bool:
    """Eldonti, hogy van-e szamjegy a szovegben.

    Ird meg a doctesteket:
    - "abc123" True
    - "abc" False
    - "" False
    """
    pass


def mask_email(email: str) -> str:
    """Egyszeru email maszkolas.

    Szabaly:
    - az @ elotti reszbol csak az elso karakter maradjon
    - utana *** kovetkezzen
    - a domain valtozatlan maradjon

    >>> mask_email("anna@example.com")
    'a***@example.com'
    >>> mask_email("b@example.com")
    'b***@example.com'
    >>> mask_email("hibas-email")
    Traceback (most recent call last):
    ...
    ValueError: invalid email
    """
    name, domain = email.split("@")
    return name + "***@" + domain


def clean_sentence(sentence: str) -> str:
    """Mondat tisztitasa: szelso szokozok levagasa, elso betu nagybetu, pont a vegere.

    Ird meg a doctesteket:
    - " alma" eredmenye "Alma."
    - "Python." eredmenye "Python."
    - "" eredmenye "."
    """
    pass


def count_words_longer_than(words: list[str], length: int) -> int:
    """Megszamolja, hany szo hosszabb a megadott hossznal.

    >>> count_words_longer_than(["alma", "fa", "korte"], 3)
    2
    >>> count_words_longer_than([], 3)
    0
    >>> count_words_longer_than(["aa", "bbb"], 3)
    0
    """
    count = 0
    for word in words:
        if len(word) >= length:
            count += 1
    return count


# 8. blokk: listak, rendezes, transzformacio


def double_numbers(numbers: list[int]) -> list[int]:
    """Minden szamot megduplaz egy uj listaban.

    Ird meg a doctesteket:
    - [1, 2, 3] eredmenye [2, 4, 6]
    - [] eredmenye []
    - [-1, 0, 2] eredmenye [-2, 0, 4]
    """
    pass


def absolute_values(numbers: list[int]) -> list[int]:
    """Visszaadja a szamok abszoluterteket.

    >>> absolute_values([-2, 0, 3])
    [2, 0, 3]
    >>> absolute_values([])
    []
    >>> absolute_values([-5])
    [5]
    """
    return numbers


def remove_negatives(numbers: list[int]) -> list[int]:
    """Eltavolitja a negativ szamokat.

    Ird meg a doctesteket:
    - [1, -2, 0, 3] eredmenye [1, 0, 3]
    - [-1, -2] eredmenye []
    - [] eredmenye []
    """
    pass


def sorted_copy(numbers: list[int]) -> list[int]:
    """Rendezett masolatot keszit, az eredeti listat nem modositja.

    >>> sorted_copy([3, 1, 2])
    [1, 2, 3]
    >>> sorted_copy([])
    []
    >>> sorted_copy([-1, -3, 2])
    [-3, -1, 2]
    """
    numbers.sort()
    return numbers


def unique_items(items: list[int]) -> list[int]:
    """Visszaadja az elemeket elso elofordulasi sorrendben, ismetles nelkul.

    Ird meg a doctesteket:
    - [1, 2, 1, 3, 2] eredmenye [1, 2, 3]
    - [] eredmenye []
    - [5, 5, 5] eredmenye [5]
    """
    pass


def merge_lists(a: list[int], b: list[int]) -> list[int]:
    """Ket listat osszefuz egy uj listaba.

    >>> merge_lists([1, 2], [3])
    [1, 2, 3]
    >>> merge_lists([], [1])
    [1]
    >>> merge_lists([1], [])
    [1]
    """
    a.extend(b)
    return a


def second_largest(numbers: list[int]) -> int:
    """Visszaadja a masodik legnagyobb kulonbozo erteket.

    Ird meg a doctesteket:
    - [1, 3, 2] eredmenye 2
    - [5, 5, 4] eredmenye 4
    - [1] eseten ValueError: not enough unique values
    """
    pass


# 9. blokk: szotarak


def get_score(scores: dict[str, int], name: str) -> int:
    """Visszaadja egy hallgato pontszamat.

    >>> get_score({"Anna": 12, "Bela": 9}, "Anna")
    12
    >>> get_score({"Anna": 12}, "Cecil")
    0
    """
    return scores[name]


def add_score(scores: dict[str, int], name: str, point: int) -> dict[str, int]:
    """Uj pontszamot ad a szotarhoz es visszaadja a szotarat.

    Ird meg a doctesteket:
    - ures szotarba Anna 10
    - meglevo Anna erteket irja felul 12-re
    """
    pass


def total_score(scores: dict[str, int]) -> int:
    """Osszegzi a pontszamokat.

    >>> total_score({"Anna": 10, "Bela": 5})
    15
    >>> total_score({})
    0
    """
    total = 0
    for key in scores:
        total += key
    return total


def best_student(scores: dict[str, int]) -> str:
    """Visszaadja a legmagasabb pontszamu hallgato nevet.

    Ird meg a doctesteket:
    - {"Anna": 10, "Bela": 12} eredmenye "Bela"
    - {"Anna": 10} eredmenye "Anna"
    - ures szotar eseten ValueError: empty scores
    """
    pass


def count_letters(text: str) -> dict[str, int]:
    """Megszamolja a betuk elofordulasat kisbetusitve.

    >>> count_letters("alma")
    {'a': 2, 'l': 1, 'm': 1}
    >>> count_letters("")
    {}
    >>> count_letters("Aa")
    {'a': 2}
    """
    result = {}
    for char in text:
        result[char] = 1
    return result


# 10. blokk: mini algoritmusok


def factorial(n: int) -> int:
    """Kiszamolja n faktorialisat.

    Ird meg a doctesteket:
    - 0 eredmenye 1
    - 1 eredmenye 1
    - 5 eredmenye 120
    - negativ szam eseten ValueError: n must be non-negative
    """
    pass


def fibonacci(n: int) -> int:
    """Visszaadja a Fibonacci-sorozat n-edik elemet.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(6)
    8
    >>> fibonacci(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be non-negative
    """
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(n: int) -> bool:
    """Eldonti, hogy egy szam prim-e.

    Ird meg a doctesteket:
    - 2 True
    - 7 True
    - 1 False
    - 9 False
    - -3 False
    """
    pass


def fizzbuzz_value(n: int) -> str:
    """Egyetlen FizzBuzz erteket ad vissza.

    >>> fizzbuzz_value(3)
    'Fizz'
    >>> fizzbuzz_value(5)
    'Buzz'
    >>> fizzbuzz_value(15)
    'FizzBuzz'
    >>> fizzbuzz_value(2)
    '2'
    """
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    if n % 15 == 0:
        return "FizzBuzz"
    return n


def roman_one_to_five(n: int) -> str:
    """Arab szamot romai szamma alakit 1 es 5 kozott.

    Ird meg a doctesteket:
    - 1 eredmenye "I"
    - 4 eredmenye "IV"
    - 5 eredmenye "V"
    - 0 eseten ValueError: number out of range
    """
    pass


# 11. blokk: szamitasok, arak, kategoriak


def celsius_to_fahrenheit(celsius: float) -> float:
    """Celsius fokot Fahrenheit fokra valt.

    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(-40)
    -40.0
    """
    return celsius * 9 / 5


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Fahrenheit fokot Celsius fokra valt.

    Ird meg a doctesteket:
    - 32 eredmenye 0.0
    - 212 eredmenye 100.0
    - -40 eredmenye -40.0
    """
    pass


def percent_of(value: float, percent: float) -> float:
    """Kiszamolja value percent szazalekat.

    Ird meg a doctesteket:
    - 200 10%-a 20.0
    - 50 50%-a 25.0
    - 100 0%-a 0.0
    """
    pass


def apply_discount(price: float, percent: float) -> float:
    """Szazalekos kedvezmenyt alkalmaz egy arhoz.

    >>> apply_discount(1000, 10)
    900.0
    >>> apply_discount(500, 0)
    500.0
    >>> apply_discount(200, 50)
    100.0
    """
    return price - percent


def final_price(net_price: float, vat_percent: float) -> float:
    """Netto arbol brutto arat szamol.

    Ird meg a doctesteket:
    - 100 es 27 eredmenye 127.0
    - 1000 es 0 eredmenye 1000.0
    - 200 es 10 eredmenye 220.0
    """
    pass


def bmi_rounded(weight_kg: float, height_m: float) -> float:
    """BMI-t szamol egy tizedesre kerekitve.

    >>> bmi_rounded(80, 2)
    20.0
    >>> bmi_rounded(72, 1.8)
    22.2
    >>> bmi_rounded(0, 1.8)
    0.0
    """
    return weight_kg / height_m


def bmi_category(bmi_value: float) -> str:
    """BMI ertekhez kategoriat ad.

    Szabaly:
    - 18.5 alatt: "sovany"
    - 18.5-tol 24.9-ig: "normal"
    - 25-tol 29.9-ig: "tulsuly"
    - 30-tol: "elhizas"

    Ird meg a doctesteket hatarertekekkel.
    """
    pass


def ticket_price(age: int) -> int:
    """Jegyarat ad eletkor alapjan.

    Szabaly:
    - 0-5 ev: 0
    - 6-18 ev: 1500
    - 19-64 ev: 2500
    - 65 ev felett: 1200

    >>> ticket_price(5)
    0
    >>> ticket_price(6)
    1500
    >>> ticket_price(18)
    1500
    >>> ticket_price(65)
    1200
    """
    if age < 5:
        return 0
    if age < 18:
        return 1500
    if age < 65:
        return 2500
    return 1200


# 12. blokk: string feldolgozas extra


def starts_with_capital(text: str) -> bool:
    """Eldonti, hogy a szoveg nagybetuvel kezdodik-e.

    Ird meg a doctesteket:
    - "Alma" True
    - "alma" False
    - "" False
    """
    pass


def count_char(text: str, char: str) -> int:
    """Megszamolja char elofordulasat textben.

    >>> count_char("alma", "a")
    2
    >>> count_char("alma", "x")
    0
    >>> count_char("", "a")
    0
    """
    return len(text)


def replace_spaces_with_dash(text: str) -> str:
    """Szokozoket kotojelre cserel.

    Ird meg a doctesteket:
    - "alma korte" eredmenye "alma-korte"
    - "a b c" eredmenye "a-b-c"
    - "" eredmenye ""
    """
    pass


def slugify_title(title: str) -> str:
    """Egyszeru URL slugot keszit kisbetukkel es kotojelekkel.

    >>> slugify_title("Hello World")
    'hello-world'
    >>> slugify_title("  Sok   Szokoz  ")
    'sok-szokoz'
    >>> slugify_title("")
    ''
    """
    return title.lower().replace(" ", "-")


def censor_word(text: str, word: str) -> str:
    """Egy megadott szot csillagokra cserel.

    Ird meg a doctesteket:
    - "ez titok" es "titok" eredmenye "ez *****"
    - "alma alma" es "alma" eredmenye "**** ****"
    - nincs talalat eseten maradjon valtozatlan
    """
    pass


def reverse_words(sentence: str) -> str:
    """Megforditja a szavak sorrendjet.

    >>> reverse_words("alma korte barack")
    'barack korte alma'
    >>> reverse_words("egy")
    'egy'
    >>> reverse_words("")
    ''
    """
    return sentence[::-1]


def remove_punctuation(text: str) -> str:
    """Eltavolitja a .,!?: karaktereket.

    Ird meg a doctesteket:
    - "Szia!" eredmenye "Szia"
    - "a,b.c" eredmenye "abc"
    - "" eredmenye ""
    """
    pass


def middle_character(text: str) -> str:
    """Visszaadja a kozepso karaktert paratlan hosszu szovegbol.

    Paros hosszu vagy ures szoveg eseten ValueError legyen.

    Ird meg a doctesteket:
    - "abc" eredmenye "b"
    - "abcde" eredmenye "c"
    - "abcd" eseten ValueError: text length must be odd
    - "" eseten ValueError: text length must be odd
    """
    pass


# 13. blokk: listak extra algoritmusok


def all_positive(numbers: list[int]) -> bool:
    """Eldonti, hogy minden szam pozitiv-e.

    >>> all_positive([1, 2, 3])
    True
    >>> all_positive([1, 0, 3])
    False
    >>> all_positive([])
    True
    """
    for number in numbers:
        if number < 0:
            return False
    return True


def any_even(numbers: list[int]) -> bool:
    """Eldonti, hogy van-e paros szam a listaban.

    Ird meg a doctesteket:
    - [1, 3, 4] True
    - [1, 3] False
    - [] False
    """
    pass


def rotate_left(items: list[int]) -> list[int]:
    """Egy elemmel balra forgatja a listat uj listaban.

    >>> rotate_left([1, 2, 3])
    [2, 3, 1]
    >>> rotate_left([1])
    [1]
    >>> rotate_left([])
    []
    """
    return items[1:] + items[0]


def running_total(numbers: list[int]) -> list[int]:
    """Reszosszegeket tartalmazo listat keszit.

    Ird meg a doctesteket:
    - [1, 2, 3] eredmenye [1, 3, 6]
    - [] eredmenye []
    - [-1, 1, 5] eredmenye [-1, 0, 5]
    """
    pass


def differences(numbers: list[int]) -> list[int]:
    """Szomszedos elemek kulonbsegeit adja vissza.

    >>> differences([3, 5, 10])
    [2, 5]
    >>> differences([1])
    []
    >>> differences([])
    []
    """
    result = []
    for index in range(len(numbers) - 1):
        result.append(numbers[index] - numbers[index + 1])
    return result


def pair_sums(numbers: list[int]) -> list[int]:
    """Szomszedos parok osszegeit adja vissza.

    Ird meg a doctesteket:
    - [1, 2, 3] eredmenye [3, 5]
    - [5] eredmenye []
    - [] eredmenye []
    """
    pass


def remove_value(items: list[int], value: int) -> list[int]:
    """Eltavolitja value minden elofordulasat egy uj listaban.

    Ird meg a doctesteket:
    - [1, 2, 1, 3], 1 eredmenye [2, 3]
    - [1, 2], 5 eredmenye [1, 2]
    - [], 1 eredmenye []
    """
    pass


def replace_value(items: list[int], old: int, new: int) -> list[int]:
    """Lecsereli old minden elofordulasat new ertekre egy uj listaban.

    Ird meg a doctesteket:
    - [1, 2, 1], 1, 9 eredmenye [9, 2, 9]
    - [1, 2], 3, 9 eredmenye [1, 2]
    - [] eredmenye []
    """
    pass


def index_of(items: list[int], value: int) -> int:
    """Visszaadja value elso indexet, ha nincs benne, akkor -1-et.

    >>> index_of([5, 6, 7], 6)
    1
    >>> index_of([5, 6, 7], 9)
    -1
    >>> index_of([], 1)
    -1
    """
    return items.index(value)


# 14. blokk: beagyazott listak, matrixok


def row_sums(matrix: list[list[int]]) -> list[int]:
    """Matrix sorosszegeit adja vissza.

    Ird meg a doctesteket:
    - [[1, 2], [3, 4]] eredmenye [3, 7]
    - [] eredmenye []
    - [[5]] eredmenye [5]
    """
    pass


def column_sums_2x2(matrix: list[list[int]]) -> list[int]:
    """2x2-es matrix oszloposszegeit adja vissza.

    >>> column_sums_2x2([[1, 2], [3, 4]])
    [4, 6]
    >>> column_sums_2x2([[0, 0], [1, 2]])
    [1, 2]
    """
    return [sum(matrix[0]), sum(matrix[1])]


def main_diagonal_2x2(matrix: list[list[int]]) -> list[int]:
    """2x2-es matrix foatlojat adja vissza.

    Ird meg a doctesteket:
    - [[1, 2], [3, 4]] eredmenye [1, 4]
    - [[5, 6], [7, 8]] eredmenye [5, 8]
    """
    pass


def transpose_2x2(matrix: list[list[int]]) -> list[list[int]]:
    """2x2-es matrix transzponaltjat adja vissza.

    Ird meg a doctesteket:
    - [[1, 2], [3, 4]] eredmenye [[1, 3], [2, 4]]
    - [[0, 1], [2, 3]] eredmenye [[0, 2], [1, 3]]
    """
    pass


def count_matrix_value(matrix: list[list[int]], value: int) -> int:
    """Megszamolja, hanyszor szerepel value a matrixban.

    >>> count_matrix_value([[1, 2], [1, 1]], 1)
    3
    >>> count_matrix_value([], 1)
    0
    >>> count_matrix_value([[2, 3]], 1)
    0
    """
    count = 0
    for row in matrix:
        if value in row:
            count += 1
    return count


# 15. blokk: szotarak extra


def inventory_total(inventory: dict[str, int]) -> int:
    """Osszesiti a raktarkeszlet darabszamat.

    >>> inventory_total({"alma": 3, "korte": 2})
    5
    >>> inventory_total({})
    0
    """
    return len(inventory)


def in_stock(inventory: dict[str, int], item: str) -> bool:
    """Eldonti, hogy egy termek keszleten van-e legalabb 1 darabbal.

    Ird meg a doctesteket:
    - {"alma": 2}, "alma" True
    - {"alma": 0}, "alma" False
    - {}, "alma" False
    """
    pass


def update_inventory(inventory: dict[str, int], item: str, amount: int) -> dict[str, int]:
    """Hozzaad amount darabot a termek keszletehez.

    >>> update_inventory({"alma": 2}, "alma", 3)
    {'alma': 5}
    >>> update_inventory({}, "korte", 4)
    {'korte': 4}
    """
    inventory[item] = amount
    return inventory


def remove_if_zero(inventory: dict[str, int]) -> dict[str, int]:
    """Eltavolitja a 0 darabos termekeket.

    Ird meg a doctesteket:
    - {"alma": 0, "korte": 2} eredmenye {"korte": 2}
    - {"alma": 1} eredmenye {"alma": 1}
    - {} eredmenye {}
    """
    pass


def most_expensive(prices: dict[str, int]) -> str:
    """Visszaadja a legdragabb termek nevet.

    >>> most_expensive({"alma": 100, "korte": 150})
    'korte'
    >>> most_expensive({"alma": 100})
    'alma'
    >>> most_expensive({})
    Traceback (most recent call last):
    ...
    ValueError: empty prices
    """
    return max(prices)


def average_score(scores: dict[str, int]) -> float:
    """Pontszamok atlagat adja vissza.

    Ird meg a doctesteket:
    - {"Anna": 10, "Bela": 20} eredmenye 15.0
    - {"Anna": 0} eredmenye 0.0
    - ures szotar eseten ValueError: empty scores
    """
    pass


def passing_students(scores: dict[str, int], limit: int) -> list[str]:
    """Visszaadja azok nevet, akik legalabb limit pontot elertek.

    >>> passing_students({"Anna": 10, "Bela": 5, "Cecil": 7}, 7)
    ['Anna', 'Cecil']
    >>> passing_students({}, 5)
    []
    """
    result = []
    for name, point in scores.items():
        if point > limit:
            result.append(name)
    return result


# 16. blokk: vegyes mini kihivasok


def login_allowed(username: str, password: str) -> bool:
    """Egyszeru belepes ellenorzes.

    Ird meg a doctesteket:
    - "admin", "titok" True
    - "admin", "rossz" False
    - "user", "titok" False
    """
    pass


def triangle_type(a: int, b: int, c: int) -> str:
    """Haromszog tipusat adja vissza.

    Eredmenyek:
    - "invalid", ha nem szerkesztheto
    - "equilateral", ha minden oldal egyenlo
    - "isosceles", ha ket oldal egyenlo
    - "scalene", ha minden oldal kulonbozo

    Ird meg a doctesteket minden esetre.
    """
    pass


def seconds_to_time(seconds: int) -> tuple[int, int, int]:
    """Masodpercet ora, perc, masodperc harmassa alakit.

    >>> seconds_to_time(0)
    (0, 0, 0)
    >>> seconds_to_time(65)
    (0, 1, 5)
    >>> seconds_to_time(3661)
    (1, 1, 1)
    """
    minutes = seconds // 60
    return 0, minutes, seconds


def time_to_seconds(hours: int, minutes: int, seconds: int) -> int:
    """Ora, perc, masodperc harmasbol masodpercet szamol.

    Ird meg a doctesteket:
    - 0, 0, 0 eredmenye 0
    - 0, 1, 5 eredmenye 65
    - 1, 1, 1 eredmenye 3661
    """
    pass


def format_duration(seconds: int) -> str:
    """Idotartamot formaz perc es masodperc formaban.

    Ird meg a doctesteket:
    - 0 eredmenye "0m 0s"
    - 65 eredmenye "1m 5s"
    - 120 eredmenye "2m 0s"
    """
    pass


def caesar_shift_one(text: str) -> str:
    """Kisbetus angol betuket eggyel eltol, z-bol a lesz.

    Ird meg a doctesteket:
    - "abc" eredmenye "bcd"
    - "xyz" eredmenye "yza"
    - "a z!" eredmenye "b a!"
    """
    pass


def balanced_parentheses_simple(text: str) -> bool:
    """Eldonti, hogy a zarojelparok egyszeruen kiegyensulyozottak-e.

    >>> balanced_parentheses_simple("(())")
    True
    >>> balanced_parentheses_simple("(()")
    False
    >>> balanced_parentheses_simple(")(")
    False
    >>> balanced_parentheses_simple("alma")
    True
    """
    return text.count("(") == text.count(")")


def shopping_total(items: list[tuple[str, int, int]]) -> int:
    """Bevasarlolista vegosszeget szamol.

    Minden elem: (nev, darab, egysegar).

    Ird meg a doctesteket:
    - [("alma", 2, 100), ("korte", 1, 150)] eredmenye 350
    - [] eredmenye 0
    - [("ceruza", 3, 50)] eredmenye 150
    """
    pass


def top_n(numbers: list[int], n: int) -> list[int]:
    """Visszaadja a legnagyobb n szamot csokkeno sorrendben.

    >>> top_n([1, 5, 3, 2], 2)
    [5, 3]
    >>> top_n([1, 2], 5)
    [2, 1]
    >>> top_n([], 3)
    []
    """
    return sorted(numbers)[:n]


def safe_get(items: list[int], index: int) -> int | None:
    """Biztonsagos listaelem-lekerdezes.

    Ird meg a doctesteket:
    - [10, 20], 0 eredmenye 10
    - [10, 20], 5 eredmenye None
    - [10, 20], -1 eredmenye None
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
