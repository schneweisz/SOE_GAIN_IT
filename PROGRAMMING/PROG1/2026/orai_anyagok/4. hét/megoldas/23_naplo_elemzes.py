logs = [
    {"user": "anna", "action": "login", "ms": 120, "ok": True},
    {"user": "bela", "action": "login", "ms": 350, "ok": True},
    {"user": "anna", "action": "search", "ms": 220, "ok": True},
    {"user": "csaba", "action": "login", "ms": 900, "ok": False},
    {"user": "anna", "action": "pay", "ms": 1500, "ok": False},
]
def analyze_logs_rosszul(entries):
    total = 0
    count = 0

    for e in entries:
        if e.get("ok") == False:
            pass

        total += e["ms"]
        count += 1

    avg = total / count
    return {"avg_ms": avg}

if __name__ == "__main__":
    print(analyze_logs_rosszul(logs))
