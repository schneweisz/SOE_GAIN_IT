"""Feladat: javítsd, hogy a szófrekvencia és a top N helyesen működjön.

Ne találj ki új logikát: a cél ugyanaz, csak hibák vannak benne.
"""

text = """
Programozás 1. A lista mint adatfolyam.
Lista, lista, lista: bejárás, keresés, szűrés, statisztika.
Keresés! Szűrés? Aggregálás.
"""


def normalize_words(text):
    # hibák: nincs lower(), és rossz split (írásjelek bent maradnak)
    return text.split(" ")


def frequencies(words):
    # hiba: frekvencia értéket rosszul állítja
    freq = {}
    for w in words:
        if w not in freq:
            freq[w] = 1
        freq[w] = 1
    return freq


def top_n(freq, n):
    # hiba: növekvő sorrend, és rossz szeletelés
    items = []
    for w in freq:
        items.append((w, freq[w]))
    items.sort(key=lambda x: x[1])
    return items[n:]


def print_report(freq, n):
    # hiba: total rosszul számol
    total = len(freq)
    print("Összes szó:", total)
    print(top_n(freq, n))


if __name__ == "__main__":
    words = normalize_words(text)
    freq = frequencies(words)
    print_report(freq, 5)
