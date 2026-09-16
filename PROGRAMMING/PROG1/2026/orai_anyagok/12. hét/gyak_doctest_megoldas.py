"""Programozas 1. - doctest gyakorlat, megoldasok.

Futtatas terminalbol:
python -m doctest -v gyak_doctest_megoldas.py
"""


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

    >>> subtract(5, 2)
    3
    >>> subtract(2, 5)
    -3
    >>> subtract(0, 0)
    0
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
    return n * n


def rectangle_area(width: float, height: float) -> float:
    """Teglalap teruletet szamolja ki.

    >>> rectangle_area(3, 4)
    12
    >>> rectangle_area(2.5, 4)
    10.0
    """
    return width * height


def circle_area(radius: float) -> float:
    """Kor teruletet kozelito ertekkel szamolja: 3.14 * r * r.

    >>> circle_area(1)
    3.14
    >>> circle_area(2)
    12.56
    >>> circle_area(0)
    0.0
    """
    return 3.14 * radius * radius


def is_even(n: int) -> bool:
    """Eldonti, hogy egy egesz szam paros-e.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    >>> is_even(0)
    True
    >>> is_even(-2)
    True
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
    return age >= 18


def is_between(value: int, minimum: int, maximum: int) -> bool:
    """Eldonti, hogy value minimum es maximum kozott van-e, hatarokkal egyutt.

    >>> is_between(5, 0, 10)
    True
    >>> is_between(0, 0, 10)
    True
    >>> is_between(10, 0, 10)
    True
    >>> is_between(-1, 0, 10)
    False
    >>> is_between(11, 0, 10)
    False
    """
    return minimum <= value <= maximum


def can_vote(age: int, citizen: bool) -> bool:
    """Szavazhat-e valaki, ha legalabb 18 eves es allampolgar.

    >>> can_vote(18, True)
    True
    >>> can_vote(17, True)
    False
    >>> can_vote(20, False)
    False
    >>> can_vote(20, True)
    True
    """
    return age >= 18 and citizen


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

    >>> safe_divide(6, 3)
    2.0
    >>> safe_divide(5, 2)
    2.5
    >>> safe_divide(5, 0) is None
    True
    """
    if b == 0:
        return None
    return a / b


def reciprocal(n: float) -> float:
    """Visszaadja egy szam reciprokat.

    >>> reciprocal(4)
    0.25
    >>> reciprocal(0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return 1 / n


def greet(name: str) -> str:
    """Udvozlo szoveget keszit.

    >>> greet("Anna")
    'Szia, Anna!'
    >>> greet("")
    'Szia, !'
    """
    return "Szia, " + name + "!"


def first_character(text: str) -> str:
    """Visszaadja a szoveg elso karakteret.

    >>> first_character("alma")
    'a'
    >>> first_character("")
    Traceback (most recent call last):
    ...
    IndexError: string index out of range
    """
    return text[0]


def last_character(text: str) -> str:
    """Visszaadja a szoveg utolso karakteret.

    >>> last_character("alma")
    'a'
    >>> last_character("Python")
    'n'
    >>> last_character("")
    Traceback (most recent call last):
    ...
    IndexError: string index out of range
    """
    return text[-1]


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
    >>> count_vowels("Apple")
    2
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def normalize_name(name: str) -> str:
    """Nev normalizalasa: felesleges szokozok levagasa es cim forma.

    >>> normalize_name(" anna ")
    'Anna'
    >>> normalize_name("KOVACS BELA")
    'Kovacs Bela'
    >>> normalize_name("")
    ''
    """
    return name.strip().title()


def initials(full_name: str) -> str:
    """Monogramositja a nevet.

    >>> initials("Kovacs Bela")
    'K.B.'
    >>> initials("Anna")
    'A.'
    >>> initials("  nagy   eva  ")
    'N.E.'
    """
    result = ""
    for part in full_name.split():
        result += part[0].upper() + "."
    return result


def is_palindrome(text: str) -> bool:
    """Eldonti, hogy egy szoveg palindrom-e.

    >>> is_palindrome("radar")
    True
    >>> is_palindrome("alma")
    False
    >>> is_palindrome("Gorog")
    True
    >>> is_palindrome("")
    True
    """
    normalized = text.lower()
    return normalized == normalized[::-1]


def first_item(items: list[int]) -> int:
    """Visszaadja a lista elso elemet.

    >>> first_item([3, 4, 5])
    3
    >>> first_item([])
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    """
    return items[0]


def sum_numbers(numbers: list[int]) -> int:
    """Osszeadja a lista elemeit.

    >>> sum_numbers([1, 2, 3])
    6
    >>> sum_numbers([])
    0
    >>> sum_numbers([-1, 1])
    0
    """
    return sum(numbers)


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
    if not numbers:
        raise ValueError("empty list has no average")
    return sum(numbers) / len(numbers)


def maximum(numbers: list[int]) -> int:
    """Visszaadja a lista legnagyobb elemet.

    >>> maximum([1, 5, 2])
    5
    >>> maximum([-3, -1, -2])
    -1
    >>> maximum([7])
    7
    >>> maximum([])
    Traceback (most recent call last):
    ...
    ValueError: empty list has no maximum
    """
    if not numbers:
        raise ValueError("empty list has no maximum")
    return max(numbers)


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
        if number > 0:
            count += 1
    return count


def filter_even(numbers: list[int]) -> list[int]:
    """Visszaadja a paros szamokat egy uj listaban.

    >>> filter_even([1, 2, 3, 4])
    [2, 4]
    >>> filter_even([])
    []
    >>> filter_even([1, 3])
    []
    >>> filter_even([-2, -1, 0])
    [-2, 0]
    """
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


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
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def grade_text(point: int) -> str:
    """Pontszam alapjan szoveges ertekelest ad vissza.

    0-49: elegtelen
    50-64: elegseges
    65-79: kozepes
    80-89: jo
    90-100: jeles

    >>> grade_text(0)
    'elegtelen'
    >>> grade_text(49)
    'elegtelen'
    >>> grade_text(50)
    'elegseges'
    >>> grade_text(64)
    'elegseges'
    >>> grade_text(65)
    'kozepes'
    >>> grade_text(79)
    'kozepes'
    >>> grade_text(80)
    'jo'
    >>> grade_text(89)
    'jo'
    >>> grade_text(90)
    'jeles'
    >>> grade_text(100)
    'jeles'
    """
    if point < 50:
        return "elegtelen"
    if point < 65:
        return "elegseges"
    if point < 80:
        return "kozepes"
    if point < 90:
        return "jo"
    return "jeles"


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
    >>> shipping_cost(25000)
    0
    >>> shipping_cost(15000)
    990
    """
    if total >= 20000:
        return 0
    if total >= 10000:
        return 990
    return 1490


def password_strength(password: str) -> str:
    """Egyszeru jelszo erosseg vizsgalat.

    Szabaly:
    - 8 karakternel rovidebb: "gyenge"
    - van benne szam es legalabb 8 karakter: "eros"
    - egyebkent: "kozepes"

    >>> password_strength("abc")
    'gyenge'
    >>> password_strength("abcdefgh")
    'kozepes'
    >>> password_strength("abc12345")
    'eros'
    >>> password_strength("12345678")
    'eros'
    """
    if len(password) < 8:
        return "gyenge"
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    if has_digit:
        return "eros"
    return "kozepes"


def format_price(price: int) -> str:
    """Ar formazasa Ft vegzodessel.

    >>> format_price(1200)
    '1200 Ft'
    >>> format_price(0)
    '0 Ft'
    >>> format_price(-500)
    '-500 Ft'
    """
    return str(price) + " Ft"


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

    >>> word_count("alma korte")
    2
    >>> word_count("")
    0
    >>> word_count("  sok   szokoz  ")
    2
    """
    return len(text.split())


def has_duplicate(items: list[int]) -> bool:
    """Eldonti, hogy van-e ismetlodo elem a listaban.

    >>> has_duplicate([1, 2, 3])
    False
    >>> has_duplicate([1, 2, 1])
    True
    >>> has_duplicate([])
    False
    """
    return len(items) != len(set(items))


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Visszaadja a legkisebb es legnagyobb elemet.

    >>> min_max([3, 1, 5])
    (1, 5)
    >>> min_max([7])
    (7, 7)
    >>> min_max([])
    Traceback (most recent call last):
    ...
    ValueError: empty list has no min/max
    """
    if not numbers:
        raise ValueError("empty list has no min/max")
    return min(numbers), max(numbers)


def remove_spaces(text: str) -> str:
    """Eltavolitja az osszes szokozt a szovegbol.

    >>> remove_spaces("a b c")
    'abc'
    >>> remove_spaces("  alma  korte ")
    'almakorte'
    >>> remove_spaces("")
    ''
    """
    return text.replace(" ", "")


def repeat_text(text: str, count: int) -> str:
    """Megismetli a szoveget count alkalommal.

    >>> repeat_text("ha", 3)
    'hahaha'
    >>> repeat_text("x", 0)
    ''
    >>> repeat_text("", 5)
    ''
    """
    return text * count


def contains_digit(text: str) -> bool:
    """Eldonti, hogy van-e szamjegy a szovegben.

    >>> contains_digit("abc123")
    True
    >>> contains_digit("abc")
    False
    >>> contains_digit("")
    False
    """
    for char in text:
        if char.isdigit():
            return True
    return False


def mask_email(email: str) -> str:
    """Egyszeru email maszkolas.

    >>> mask_email("anna@example.com")
    'a***@example.com'
    >>> mask_email("b@example.com")
    'b***@example.com'
    >>> mask_email("hibas-email")
    Traceback (most recent call last):
    ...
    ValueError: invalid email
    """
    if "@" not in email:
        raise ValueError("invalid email")
    name, domain = email.split("@", 1)
    return name[0] + "***@" + domain


def clean_sentence(sentence: str) -> str:
    """Mondat tisztitasa: szelso szokozok levagasa, elso betu nagybetu, pont a vegere.

    >>> clean_sentence(" alma")
    'Alma.'
    >>> clean_sentence("Python.")
    'Python.'
    >>> clean_sentence("")
    '.'
    """
    cleaned = sentence.strip().capitalize()
    if cleaned.endswith("."):
        return cleaned
    return cleaned + "."


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
        if len(word) > length:
            count += 1
    return count


def double_numbers(numbers: list[int]) -> list[int]:
    """Minden szamot megduplaz egy uj listaban.

    >>> double_numbers([1, 2, 3])
    [2, 4, 6]
    >>> double_numbers([])
    []
    >>> double_numbers([-1, 0, 2])
    [-2, 0, 4]
    """
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def absolute_values(numbers: list[int]) -> list[int]:
    """Visszaadja a szamok abszoluterteket.

    >>> absolute_values([-2, 0, 3])
    [2, 0, 3]
    >>> absolute_values([])
    []
    >>> absolute_values([-5])
    [5]
    """
    result = []
    for number in numbers:
        result.append(abs(number))
    return result


def remove_negatives(numbers: list[int]) -> list[int]:
    """Eltavolitja a negativ szamokat.

    >>> remove_negatives([1, -2, 0, 3])
    [1, 0, 3]
    >>> remove_negatives([-1, -2])
    []
    >>> remove_negatives([])
    []
    """
    result = []
    for number in numbers:
        if number >= 0:
            result.append(number)
    return result


def sorted_copy(numbers: list[int]) -> list[int]:
    """Rendezett masolatot keszit, az eredeti listat nem modositja.

    >>> sorted_copy([3, 1, 2])
    [1, 2, 3]
    >>> sorted_copy([])
    []
    >>> sorted_copy([-1, -3, 2])
    [-3, -1, 2]
    """
    return sorted(numbers)


def unique_items(items: list[int]) -> list[int]:
    """Visszaadja az elemeket elso elofordulasi sorrendben, ismetles nelkul.

    >>> unique_items([1, 2, 1, 3, 2])
    [1, 2, 3]
    >>> unique_items([])
    []
    >>> unique_items([5, 5, 5])
    [5]
    """
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def merge_lists(a: list[int], b: list[int]) -> list[int]:
    """Ket listat osszefuz egy uj listaba.

    >>> merge_lists([1, 2], [3])
    [1, 2, 3]
    >>> merge_lists([], [1])
    [1]
    >>> merge_lists([1], [])
    [1]
    """
    return a + b


def second_largest(numbers: list[int]) -> int:
    """Visszaadja a masodik legnagyobb kulonbozo erteket.

    >>> second_largest([1, 3, 2])
    2
    >>> second_largest([5, 5, 4])
    4
    >>> second_largest([1])
    Traceback (most recent call last):
    ...
    ValueError: not enough unique values
    """
    unique = sorted(set(numbers))
    if len(unique) < 2:
        raise ValueError("not enough unique values")
    return unique[-2]


def get_score(scores: dict[str, int], name: str) -> int:
    """Visszaadja egy hallgato pontszamat.

    >>> get_score({"Anna": 12, "Bela": 9}, "Anna")
    12
    >>> get_score({"Anna": 12}, "Cecil")
    0
    """
    return scores.get(name, 0)


def add_score(scores: dict[str, int], name: str, point: int) -> dict[str, int]:
    """Uj pontszamot ad a szotarhoz es visszaadja a szotarat.

    >>> add_score({}, "Anna", 10)
    {'Anna': 10}
    >>> add_score({"Anna": 10}, "Anna", 12)
    {'Anna': 12}
    """
    scores[name] = point
    return scores


def total_score(scores: dict[str, int]) -> int:
    """Osszegzi a pontszamokat.

    >>> total_score({"Anna": 10, "Bela": 5})
    15
    >>> total_score({})
    0
    """
    return sum(scores.values())


def best_student(scores: dict[str, int]) -> str:
    """Visszaadja a legmagasabb pontszamu hallgato nevet.

    >>> best_student({"Anna": 10, "Bela": 12})
    'Bela'
    >>> best_student({"Anna": 10})
    'Anna'
    >>> best_student({})
    Traceback (most recent call last):
    ...
    ValueError: empty scores
    """
    if not scores:
        raise ValueError("empty scores")
    best_name = ""
    best_point = None
    for name, point in scores.items():
        if best_point is None or point > best_point:
            best_name = name
            best_point = point
    return best_name


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
    for char in text.lower():
        result[char] = result.get(char, 0) + 1
    return result


def factorial(n: int) -> int:
    """Kiszamolja n faktorialisat.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be non-negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


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
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


def is_prime(n: int) -> bool:
    """Eldonti, hogy egy szam prim-e.

    >>> is_prime(2)
    True
    >>> is_prime(7)
    True
    >>> is_prime(1)
    False
    >>> is_prime(9)
    False
    >>> is_prime(-3)
    False
    """
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


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
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def roman_one_to_five(n: int) -> str:
    """Arab szamot romai szamma alakit 1 es 5 kozott.

    >>> roman_one_to_five(1)
    'I'
    >>> roman_one_to_five(4)
    'IV'
    >>> roman_one_to_five(5)
    'V'
    >>> roman_one_to_five(0)
    Traceback (most recent call last):
    ...
    ValueError: number out of range
    """
    values = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
    if n not in values:
        raise ValueError("number out of range")
    return values[n]


def celsius_to_fahrenheit(celsius: float) -> float:
    """Celsius fokot Fahrenheit fokra valt.

    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(-40)
    -40.0
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Fahrenheit fokot Celsius fokra valt.

    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(212)
    100.0
    >>> fahrenheit_to_celsius(-40)
    -40.0
    """
    return (fahrenheit - 32) * 5 / 9


def percent_of(value: float, percent: float) -> float:
    """Kiszamolja value percent szazalekat.

    >>> percent_of(200, 10)
    20.0
    >>> percent_of(50, 50)
    25.0
    >>> percent_of(100, 0)
    0.0
    """
    return value * percent / 100


def apply_discount(price: float, percent: float) -> float:
    """Szazalekos kedvezmenyt alkalmaz egy arhoz.

    >>> apply_discount(1000, 10)
    900.0
    >>> apply_discount(500, 0)
    500.0
    >>> apply_discount(200, 50)
    100.0
    """
    return price - price * percent / 100


def final_price(net_price: float, vat_percent: float) -> float:
    """Netto arbol brutto arat szamol.

    >>> final_price(100, 27)
    127.0
    >>> final_price(1000, 0)
    1000.0
    >>> final_price(200, 10)
    220.0
    """
    return net_price + net_price * vat_percent / 100


def bmi_rounded(weight_kg: float, height_m: float) -> float:
    """BMI-t szamol egy tizedesre kerekitve.

    >>> bmi_rounded(80, 2)
    20.0
    >>> bmi_rounded(72, 1.8)
    22.2
    >>> bmi_rounded(0, 1.8)
    0.0
    """
    return round(weight_kg / (height_m * height_m), 1)


def bmi_category(bmi_value: float) -> str:
    """BMI ertekhez kategoriat ad.

    >>> bmi_category(18.4)
    'sovany'
    >>> bmi_category(18.5)
    'normal'
    >>> bmi_category(24.9)
    'normal'
    >>> bmi_category(25)
    'tulsuly'
    >>> bmi_category(30)
    'elhizas'
    """
    if bmi_value < 18.5:
        return "sovany"
    if bmi_value < 25:
        return "normal"
    if bmi_value < 30:
        return "tulsuly"
    return "elhizas"


def ticket_price(age: int) -> int:
    """Jegyarat ad eletkor alapjan.

    >>> ticket_price(5)
    0
    >>> ticket_price(6)
    1500
    >>> ticket_price(18)
    1500
    >>> ticket_price(19)
    2500
    >>> ticket_price(64)
    2500
    >>> ticket_price(65)
    1200
    """
    if age <= 5:
        return 0
    if age <= 18:
        return 1500
    if age <= 64:
        return 2500
    return 1200


def starts_with_capital(text: str) -> bool:
    """Eldonti, hogy a szoveg nagybetuvel kezdodik-e.

    >>> starts_with_capital("Alma")
    True
    >>> starts_with_capital("alma")
    False
    >>> starts_with_capital("")
    False
    """
    return bool(text) and text[0].isupper()


def count_char(text: str, char: str) -> int:
    """Megszamolja char elofordulasat textben.

    >>> count_char("alma", "a")
    2
    >>> count_char("alma", "x")
    0
    >>> count_char("", "a")
    0
    """
    return text.count(char)


def replace_spaces_with_dash(text: str) -> str:
    """Szokozoket kotojelre cserel.

    >>> replace_spaces_with_dash("alma korte")
    'alma-korte'
    >>> replace_spaces_with_dash("a b c")
    'a-b-c'
    >>> replace_spaces_with_dash("")
    ''
    """
    return text.replace(" ", "-")


def slugify_title(title: str) -> str:
    """Egyszeru URL slugot keszit kisbetukkel es kotojelekkel.

    >>> slugify_title("Hello World")
    'hello-world'
    >>> slugify_title("  Sok   Szokoz  ")
    'sok-szokoz'
    >>> slugify_title("")
    ''
    """
    return "-".join(title.lower().split())


def censor_word(text: str, word: str) -> str:
    """Egy megadott szot csillagokra cserel.

    >>> censor_word("ez titok", "titok")
    'ez *****'
    >>> censor_word("alma alma", "alma")
    '**** ****'
    >>> censor_word("nincs talalat", "alma")
    'nincs talalat'
    """
    return text.replace(word, "*" * len(word))


def reverse_words(sentence: str) -> str:
    """Megforditja a szavak sorrendjet.

    >>> reverse_words("alma korte barack")
    'barack korte alma'
    >>> reverse_words("egy")
    'egy'
    >>> reverse_words("")
    ''
    """
    return " ".join(reversed(sentence.split()))


def remove_punctuation(text: str) -> str:
    """Eltavolitja a .,!?: karaktereket.

    >>> remove_punctuation("Szia!")
    'Szia'
    >>> remove_punctuation("a,b.c")
    'abc'
    >>> remove_punctuation("")
    ''
    """
    result = ""
    for char in text:
        if char not in ".,!?:": 
            result += char
    return result


def middle_character(text: str) -> str:
    """Visszaadja a kozepso karaktert paratlan hosszu szovegbol.

    >>> middle_character("abc")
    'b'
    >>> middle_character("abcde")
    'c'
    >>> middle_character("abcd")
    Traceback (most recent call last):
    ...
    ValueError: text length must be odd
    >>> middle_character("")
    Traceback (most recent call last):
    ...
    ValueError: text length must be odd
    """
    if len(text) == 0 or len(text) % 2 == 0:
        raise ValueError("text length must be odd")
    return text[len(text) // 2]


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
        if number <= 0:
            return False
    return True


def any_even(numbers: list[int]) -> bool:
    """Eldonti, hogy van-e paros szam a listaban.

    >>> any_even([1, 3, 4])
    True
    >>> any_even([1, 3])
    False
    >>> any_even([])
    False
    """
    for number in numbers:
        if number % 2 == 0:
            return True
    return False


def rotate_left(items: list[int]) -> list[int]:
    """Egy elemmel balra forgatja a listat uj listaban.

    >>> rotate_left([1, 2, 3])
    [2, 3, 1]
    >>> rotate_left([1])
    [1]
    >>> rotate_left([])
    []
    """
    if not items:
        return []
    return items[1:] + [items[0]]


def running_total(numbers: list[int]) -> list[int]:
    """Reszosszegeket tartalmazo listat keszit.

    >>> running_total([1, 2, 3])
    [1, 3, 6]
    >>> running_total([])
    []
    >>> running_total([-1, 1, 5])
    [-1, 0, 5]
    """
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)
    return result


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
        result.append(numbers[index + 1] - numbers[index])
    return result


def pair_sums(numbers: list[int]) -> list[int]:
    """Szomszedos parok osszegeit adja vissza.

    >>> pair_sums([1, 2, 3])
    [3, 5]
    >>> pair_sums([5])
    []
    >>> pair_sums([])
    []
    """
    result = []
    for index in range(len(numbers) - 1):
        result.append(numbers[index] + numbers[index + 1])
    return result


def remove_value(items: list[int], value: int) -> list[int]:
    """Eltavolitja value minden elofordulasat egy uj listaban.

    >>> remove_value([1, 2, 1, 3], 1)
    [2, 3]
    >>> remove_value([1, 2], 5)
    [1, 2]
    >>> remove_value([], 1)
    []
    """
    result = []
    for item in items:
        if item != value:
            result.append(item)
    return result


def replace_value(items: list[int], old: int, new: int) -> list[int]:
    """Lecsereli old minden elofordulasat new ertekre egy uj listaban.

    >>> replace_value([1, 2, 1], 1, 9)
    [9, 2, 9]
    >>> replace_value([1, 2], 3, 9)
    [1, 2]
    >>> replace_value([], 1, 9)
    []
    """
    result = []
    for item in items:
        if item == old:
            result.append(new)
        else:
            result.append(item)
    return result


def index_of(items: list[int], value: int) -> int:
    """Visszaadja value elso indexet, ha nincs benne, akkor -1-et.

    >>> index_of([5, 6, 7], 6)
    1
    >>> index_of([5, 6, 7], 9)
    -1
    >>> index_of([], 1)
    -1
    """
    for index, item in enumerate(items):
        if item == value:
            return index
    return -1


def row_sums(matrix: list[list[int]]) -> list[int]:
    """Matrix sorosszegeit adja vissza.

    >>> row_sums([[1, 2], [3, 4]])
    [3, 7]
    >>> row_sums([])
    []
    >>> row_sums([[5]])
    [5]
    """
    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums_2x2(matrix: list[list[int]]) -> list[int]:
    """2x2-es matrix oszloposszegeit adja vissza.

    >>> column_sums_2x2([[1, 2], [3, 4]])
    [4, 6]
    >>> column_sums_2x2([[0, 0], [1, 2]])
    [1, 2]
    """
    return [matrix[0][0] + matrix[1][0], matrix[0][1] + matrix[1][1]]


def main_diagonal_2x2(matrix: list[list[int]]) -> list[int]:
    """2x2-es matrix foatlojat adja vissza.

    >>> main_diagonal_2x2([[1, 2], [3, 4]])
    [1, 4]
    >>> main_diagonal_2x2([[5, 6], [7, 8]])
    [5, 8]
    """
    return [matrix[0][0], matrix[1][1]]


def transpose_2x2(matrix: list[list[int]]) -> list[list[int]]:
    """2x2-es matrix transzponaltjat adja vissza.

    >>> transpose_2x2([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    >>> transpose_2x2([[0, 1], [2, 3]])
    [[0, 2], [1, 3]]
    """
    return [[matrix[0][0], matrix[1][0]], [matrix[0][1], matrix[1][1]]]


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
        for item in row:
            if item == value:
                count += 1
    return count


def inventory_total(inventory: dict[str, int]) -> int:
    """Osszesiti a raktarkeszlet darabszamat.

    >>> inventory_total({"alma": 3, "korte": 2})
    5
    >>> inventory_total({})
    0
    """
    return sum(inventory.values())


def in_stock(inventory: dict[str, int], item: str) -> bool:
    """Eldonti, hogy egy termek keszleten van-e legalabb 1 darabbal.

    >>> in_stock({"alma": 2}, "alma")
    True
    >>> in_stock({"alma": 0}, "alma")
    False
    >>> in_stock({}, "alma")
    False
    """
    return inventory.get(item, 0) > 0


def update_inventory(inventory: dict[str, int], item: str, amount: int) -> dict[str, int]:
    """Hozzaad amount darabot a termek keszletehez.

    >>> update_inventory({"alma": 2}, "alma", 3)
    {'alma': 5}
    >>> update_inventory({}, "korte", 4)
    {'korte': 4}
    """
    inventory[item] = inventory.get(item, 0) + amount
    return inventory


def remove_if_zero(inventory: dict[str, int]) -> dict[str, int]:
    """Eltavolitja a 0 darabos termekeket.

    >>> remove_if_zero({"alma": 0, "korte": 2})
    {'korte': 2}
    >>> remove_if_zero({"alma": 1})
    {'alma': 1}
    >>> remove_if_zero({})
    {}
    """
    result = {}
    for item, amount in inventory.items():
        if amount != 0:
            result[item] = amount
    return result


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
    if not prices:
        raise ValueError("empty prices")
    best_name = ""
    best_price = None
    for name, price in prices.items():
        if best_price is None or price > best_price:
            best_name = name
            best_price = price
    return best_name


def average_score(scores: dict[str, int]) -> float:
    """Pontszamok atlagat adja vissza.

    >>> average_score({"Anna": 10, "Bela": 20})
    15.0
    >>> average_score({"Anna": 0})
    0.0
    >>> average_score({})
    Traceback (most recent call last):
    ...
    ValueError: empty scores
    """
    if not scores:
        raise ValueError("empty scores")
    return sum(scores.values()) / len(scores)


def passing_students(scores: dict[str, int], limit: int) -> list[str]:
    """Visszaadja azok nevet, akik legalabb limit pontot elertek.

    >>> passing_students({"Anna": 10, "Bela": 5, "Cecil": 7}, 7)
    ['Anna', 'Cecil']
    >>> passing_students({}, 5)
    []
    """
    result = []
    for name, point in scores.items():
        if point >= limit:
            result.append(name)
    return result


def login_allowed(username: str, password: str) -> bool:
    """Egyszeru belepes ellenorzes.

    >>> login_allowed("admin", "titok")
    True
    >>> login_allowed("admin", "rossz")
    False
    >>> login_allowed("user", "titok")
    False
    """
    return username == "admin" and password == "titok"


def triangle_type(a: int, b: int, c: int) -> str:
    """Haromszog tipusat adja vissza.

    >>> triangle_type(1, 2, 3)
    'invalid'
    >>> triangle_type(3, 3, 3)
    'equilateral'
    >>> triangle_type(3, 3, 2)
    'isosceles'
    >>> triangle_type(3, 4, 5)
    'scalene'
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"


def seconds_to_time(seconds: int) -> tuple[int, int, int]:
    """Masodpercet ora, perc, masodperc harmassa alakit.

    >>> seconds_to_time(0)
    (0, 0, 0)
    >>> seconds_to_time(65)
    (0, 1, 5)
    >>> seconds_to_time(3661)
    (1, 1, 1)
    """
    hours = seconds // 3600
    remaining = seconds % 3600
    minutes = remaining // 60
    seconds_left = remaining % 60
    return hours, minutes, seconds_left


def time_to_seconds(hours: int, minutes: int, seconds: int) -> int:
    """Ora, perc, masodperc harmasbol masodpercet szamol.

    >>> time_to_seconds(0, 0, 0)
    0
    >>> time_to_seconds(0, 1, 5)
    65
    >>> time_to_seconds(1, 1, 1)
    3661
    """
    return hours * 3600 + minutes * 60 + seconds


def format_duration(seconds: int) -> str:
    """Idotartamot formaz perc es masodperc formaban.

    >>> format_duration(0)
    '0m 0s'
    >>> format_duration(65)
    '1m 5s'
    >>> format_duration(120)
    '2m 0s'
    """
    minutes = seconds // 60
    seconds_left = seconds % 60
    return str(minutes) + "m " + str(seconds_left) + "s"


def caesar_shift_one(text: str) -> str:
    """Kisbetus angol betuket eggyel eltol, z-bol a lesz.

    >>> caesar_shift_one("abc")
    'bcd'
    >>> caesar_shift_one("xyz")
    'yza'
    >>> caesar_shift_one("a z!")
    'b a!'
    """
    result = ""
    for char in text:
        if char == "z":
            result += "a"
        elif "a" <= char <= "y":
            result += chr(ord(char) + 1)
        else:
            result += char
    return result


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
    balance = 0
    for char in text:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


def shopping_total(items: list[tuple[str, int, int]]) -> int:
    """Bevasarlolista vegosszeget szamol.

    Minden elem: (nev, darab, egysegar).

    >>> shopping_total([("alma", 2, 100), ("korte", 1, 150)])
    350
    >>> shopping_total([])
    0
    >>> shopping_total([("ceruza", 3, 50)])
    150
    """
    total = 0
    for _name, quantity, price in items:
        total += quantity * price
    return total


def top_n(numbers: list[int], n: int) -> list[int]:
    """Visszaadja a legnagyobb n szamot csokkeno sorrendben.

    >>> top_n([1, 5, 3, 2], 2)
    [5, 3]
    >>> top_n([1, 2], 5)
    [2, 1]
    >>> top_n([], 3)
    []
    """
    return sorted(numbers, reverse=True)[:n]


def safe_get(items: list[int], index: int) -> int | None:
    """Biztonsagos listaelem-lekerdezes.

    >>> safe_get([10, 20], 0)
    10
    >>> safe_get([10, 20], 5) is None
    True
    >>> safe_get([10, 20], -1) is None
    True
    """
    if index < 0 or index >= len(items):
        return None
    return items[index]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
