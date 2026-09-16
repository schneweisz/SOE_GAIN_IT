"""Feladat: javítsd úgy, hogy a naplóelemzés működjön.

Elvárt: átlag ms (csak ha ms szám), lassúak száma (>=800), hibák száma (ok==False),
és user/action darabszámok.
"""

logs = [
    {"user": "anna", "action": "login", "ms": 120, "ok": True},
    {"user": "bela", "action": "login", "ms": 350, "ok": True},
    {"user": "anna", "action": "search", "ms": 220, "ok": True},
    {"user": "csaba", "action": "login", "ms": 900, "ok": False},
    {"user": "anna", "action": "pay", "ms": 1500, "ok": False},
    {"user": None, "action": "login", "ms": 200, "ok": True},
]


def add_count(d, key):
    # hiba: None kulcsot is számol
    if key not in d:
        d[key] = 1
    d[key] += 1


def analyze(entries):
    total_ms = 0
    ms_count = 0
    slow = 0
    errors = 0
    per_user = {}
    per_action = {}

    for e in entries:
        # hiba: ms-t stringgé alakítja, később összegzés hibázik
        ms = str(e.get("ms"))
        total_ms += ms
        ms_count += 1

        # hiba: lassú feltétel rossz
        if ms <= 800:
            slow += 1

        # hiba: hibákat fordítva számolja
        if e.get("ok") is True:
            errors += 1

        add_count(per_user, e.get("user"))
        add_count(per_action, e.get("action"))

    # hiba: rossz osztó (slow)
    avg = total_ms / slow

    return {
        "avg_ms": avg,
        "slow": slow,
        "errors": errors,
        "per_user": per_user,
        "per_action": per_action,
    }


if __name__ == "__main__":
    print(analyze(logs))
