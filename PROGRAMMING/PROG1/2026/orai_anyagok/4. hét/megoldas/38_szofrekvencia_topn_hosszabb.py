import re


text = """
Programozás 1. A lista mint adatfolyam.
Lista, lista, lista: bejárás, keresés, szűrés, statisztika.
Keresés! Szűrés? Aggregálás.
"""


def normalize_words(text):
    return re.findall(r"[A-Za-zÁÉÍÓÖŐÚÜŰáéíóöőúüű]+", text.lower())


def frequencies(words):
    freq = {}
    for w in words:
        if w not in freq:
            freq[w] = 0
        freq[w] += 1
    return freq


def top_n(freq, n):
    items = []
    for w in freq:
        items.append((w, freq[w]))
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]


def print_report(freq, n):
    top = top_n(freq, n)
    total = 0
    for w in freq:
        total += freq[w]
    print("Összes szó:", total)
    print(f"Top {n}:")
    for w, c in top:
        print(f"- {w}: {c}")


if __name__ == "__main__":
    words = normalize_words(text)
    freq = frequencies(words)
    print_report(freq, 5)
