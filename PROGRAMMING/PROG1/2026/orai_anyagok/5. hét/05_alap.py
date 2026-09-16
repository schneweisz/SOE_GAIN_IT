from datetime import datetime
from itertools import groupby
from statistics import mean


# =========================
# Adathalmazok
# =========================

students = [
    {"neptun": "ABC123", "name": "Nagy Anna", "zh": 78, "hf": 92, "bonus": 2},
    {"neptun": "QWE987", "name": "Kiss Béla", "zh": 91, "hf": 61, "bonus": 0},
    {"neptun": "HJK555", "name": "Tóth Csilla", "zh": 78, "hf": 92, "bonus": 0},
    {"neptun": "ZXC111", "name": "Szabó Dénes", "zh": 60, "hf": 90, "bonus": 5},
]

alerts = [
    {"id": "A1", "severity": "WARN", "ts": "2026-03-11T09:01:00", "service": "auth"},
    {"id": "A2", "severity": "CRIT", "ts": "2026-03-11T09:00:59", "service": "report"},
    {"id": "A3", "severity": "INFO", "ts": "2026-03-11T09:00:58", "service": "auth"},
    {"id": "A4", "severity": "ERROR", "ts": "2026-03-11T09:01:02", "service": "profile"},
    {"id": "A5", "severity": "CRIT", "ts": "2026-03-11T09:01:01", "service": "auth"},
]

logs = [
    {"ts": "11/03/2026 09:12:03", "endpoint": "/api/login", "status": 200, "rt_ms": 41},
    {"ts": "11/03/2026 09:12:04", "endpoint": "/api/login", "status": 429, "rt_ms": 12},
    {"ts": "11/03/2026 09:12:05", "endpoint": "/api/report", "status": 500, "rt_ms": 930},
    {"ts": "11/03/2026 09:12:06", "endpoint": "/api/report", "status": 200, "rt_ms": 310},
    {"ts": "11/03/2026 09:12:07", "endpoint": "/api/profile", "status": 200, "rt_ms": 88},
]

files = [
    {"path": "notes.pdf", "size": "1.2MB"},
    {"path": "raw.bin", "size": "900KB"},
    {"path": "img.png", "size": "120KB"},
    {"path": "backup.zip", "size": "3.5MB"},
]

versions = ["1.2.0", "1.10.0", "1.2.11", "2.0.0", "1.2.3"]

transactions = [
    {"id": "T100", "user": "u1", "amount": "-12000", "currency": "HUF", "ts": "2026-03-11T09:10:00"},
    {"id": "T101", "user": "u2", "amount": "2500", "currency": "HUF", "ts": "2026-03-11T09:10:02"},
    {"id": "T102", "user": "u1", "amount": "-2500", "currency": "HUF", "ts": "2026-03-11T09:10:03"},
    {"id": "T103", "user": "u3", "amount": "2500", "currency": "HUF", "ts": "2026-03-11T09:10:01"},
]

readings = [
    {"device": "d1", "ts": "2026-03-11T09:00:02", "value": 20.1},
    {"device": "d2", "ts": "2026-03-11T09:00:01", "value": 18.9},
    {"device": "d1", "ts": "2026-03-11T09:00:01", "value": 20.0},
    {"device": "d2", "ts": "2026-03-11T09:00:03", "value": 19.2},
    {"device": "d1", "ts": "2026-03-11T09:00:03", "value": 20.2},
]

ips = ["10.0.0.2", "10.0.0.12", "192.168.1.1", "10.0.0.3", "172.16.0.5"]

results = [
    {"name": "Nagy Anna", "points": 84},
    {"name": "Kiss Béla", "points": 59},
    {"name": "Tóth Csilla", "points": 84},
    {"name": "Szabó Dénes", "points": 41},
    {"name": "Varga Erika", "points": 73},
]

names = ["  Kiss Béla", "nagy anna", "Tóth Csilla ", "NAGY ANNA", "Árva Éva"]

ticket_ids = ["ID1", "ID2", "ID10", "ID3", "ID21", "ID11"]

hits = [
    {"ts": "2026-03-10T23:59:59", "endpoint": "/api/login", "status": 200},
    {"ts": "2026-03-11T00:00:01", "endpoint": "/api/login", "status": 500},
    {"ts": "2026-03-11T00:00:02", "endpoint": "/api/login", "status": 200},
    {"ts": "2026-03-11T00:00:03", "endpoint": "/api/report", "status": 200},
    {"ts": "2026-03-10T12:00:00", "endpoint": "/api/report", "status": 503},
]

dirty = [
    {"id": "A", "score": "10"},
    {"id": "B", "score": None},
    {"id": "C"},
    {"id": "D", "score": "2"},
]


# =========================
# Segéd fgv-ek
# =========================

def parse_ts_ddmmyyyy_hhmmss(value):
    """Időbélyeg parszeolása DD/MM/YYYY HH:MM:SS formátumból."""
    return datetime.strptime(value, "%d/%m/%Y %H:%M:%S")


def parse_ts_iso(value):
    """Időbélyeg parszeolása ISO 8601 formátumból (YYYY-MM-DDTHH:MM:SS)."""
    return datetime.fromisoformat(value)


def parse_iso_from_dict(item, field="ts"):
    """Szótárból ISO formátumú időbélyeget kiemeli és parszeol (alapértékezett 'ts' mező)."""
    return parse_ts_iso(item[field])


def safe_int(value):
    """Biztonságosan konvertál szövegből egész számmá; None vagy konverziós hiba esetén None-t ad vissza."""
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def safe_sorted(items, *, key, reverse=False):
    """Rendezés úgy, hogy a key hibája esetén az elem a végére kerüljön."""

    def safe_key(item):
        try:
            return (0, key(item))
        except Exception:
            return (1, None)

    return sorted(items, key=safe_key, reverse=reverse)


def take_top_n(items, n, *, key):
    """A `key` függvény szerint csökkenő sorrendben rendez, és visszaadja az első `n` elemet."""
    return sorted(items, key=key, reverse=True)[:n]


# =========================
# 1.1 Tanulmányi eredmények 
# =========================




# =========================
# 1.3 Alerts
# =========================



# =========================
# 1.2 Logok 
# =========================



# =========================
# 2.4 Fájlméretek 
# =========================




# =========================
# 2.5 Verziók 
# =========================




# =========================
# 2.1 Tranzakciók 
# =========================


# =========================
# 3.4 IP rendezés
# =========================



# =========================
# 3.5 Tranzakciók user-összegzés 
# =========================


# =========================
# 2.2 Log riport rendezése
# =========================


# =========================
# 3.6 Stabil rendezés több lépésben 
# =========================




# =========================
# 2.3 max/min tie-break 
# =========================



# =========================
# 3.1 Szenzorok groupby 
# =========================



# =========================
# 3.2 Endpoint összegzés groupby-val
# =========================


# =========================
# 3.3 Biztonságos rendezés
# =========================


# =========================
# 3.7 Jegyek + groupby – megoldás
# =========================



# =========================
# 2.6 Case-insensitive rendezés – megoldás
# =========================

# =========================
# 2.7 Természetes rendezés ID-kre – megoldás
# =========================


# =========================
# 3.8 Napi endpoint riport – megoldás
# =========================


# =========================
# Demo futtatás
# =========================

if __name__ == "__main__":
    # Itt lehet meghívni a fenti függvényeket és kiírni az eredményeket teszteléshez
    pass