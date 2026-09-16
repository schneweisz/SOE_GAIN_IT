logs = [
    {"user": "anna", "action": "login", "ms": 120, "ok": True},
    {"user": "bela", "action": "login", "ms": 350, "ok": True},
    {"user": "anna", "action": "search", "ms": 220, "ok": True},
    {"user": "csaba", "action": "login", "ms": 900, "ok": False},
    {"user": "anna", "action": "pay", "ms": 1500, "ok": False},
    {"user": "bela", "action": "search", "ms": 180, "ok": True},
    {"user": "bela", "action": "pay", "ms": 800, "ok": True},
    {"user": "anna", "action": "logout", "ms": 60, "ok": True},
    {"user": "csaba", "action": "login", "ms": 400, "ok": True},
    {"user": None, "action": "login", "ms": 200, "ok": True},
]


def add_count(d, key):
    if key is None:
        return
    if key not in d:
        d[key] = 0
    d[key] += 1


def analyze(entries):
    total_ms = 0
    ms_count = 0
    slow = 0
    errors = 0
    per_user = {}
    per_action = {}

    for e in entries:
        ms = e.get("ms")
        if isinstance(ms, int):
            total_ms += ms
            ms_count += 1
            if ms >= 800:
                slow += 1

        if e.get("ok") is False:
            errors += 1

        add_count(per_user, e.get("user"))
        add_count(per_action, e.get("action"))

    avg = None if ms_count == 0 else total_ms / ms_count

    top_user = None
    top_user_count = None
    for u in per_user:
        c = per_user[u]
        if top_user_count is None or c > top_user_count:
            top_user = u
            top_user_count = c

    return {
        "avg_ms": avg,
        "slow": slow,
        "errors": errors,
        "per_user": per_user,
        "per_action": per_action,
        "top_user": top_user,
    }


if __name__ == "__main__":
    r = analyze(logs)
    print("Átlag ms:", r["avg_ms"])
    print("Lassú (>=800ms):", r["slow"])
    print("Hibák:", r["errors"])
    print("User bontás:", r["per_user"])
    print("Action bontás:", r["per_action"])
    print("Top user:", r["top_user"])
