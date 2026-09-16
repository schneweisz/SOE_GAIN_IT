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
# {"neptun": "ABC123", "name": "Nagy Anna", "zh": 78, "hf": 92, "bonus": 2},
def finals_points(s):
    return 0.7*float(s["zh"]) + 0.3 * float(s["hf"]) + float(s.get("bonus",0))

def student_ranking(data):
    return sorted(
        data,
        key=lambda s:(-finals_points(s), -float(s["zh"]),s["name"])
    )



# =========================
# 1.3 Alerts
# =========================
#{"id": "A1", "severity": "WARN", "ts": "2026-03-11T09:01:00", "service": "auth"},

SEVERITY_ORDER={"INFO":0,"WARN":1,"ERROR":2,"CRIT":3}

#FG. hogy szám alapján tudjunk rendezni, mert a stringet "számmá alakítottuk"
def severity_rank(alert):
    return SEVERITY_ORDER.get(str(alert.get("severity","")),-1)

def alerts_sorted(data):
    return sorted(
        data,
        key=lambda a: (
            -severity_rank(a),
            datetime.max - parse_ts_iso(a["ts"]),
            a["id"],
        )
    )


# =========================
# 1.2 Logok 
# =========================
#{"ts": "11/03/2026 09:12:03", "endpoint": "/api/login", "status": 200, "rt_ms": 41},
def parse_ts_log(log):
    return parse_ts_ddmmyyyy_hhmmss(log["ts"])

def logs_time_sorted(data):
    return sorted(data,key=parse_ts_log)

def slowest_logs(data,n=2):
    return sorted(data,key=lambda l:l["rt_ms"], reverse=True)[:n]


# =========================
# 2.4 Fájlméretek 
# =========================
#{"path": "notes.pdf", "size": "1.2MB"},
#{"path": "raw.bin", "size": "900KB"},
#{"path": "img.png", "size": "120KB"},
#{"path": "backup.zip", "size": "3.5MB"},

SIZE_MULTIPLIERS={"B":1,"KB":1024,"MB":1024**2,"GB":1024**3}

def parse_size_to_bytes(size):
    s=size.strip().upper() #" 1.2 mb   " -> "1.2 MB", 
    s=s.replace(" ","") #"1.2 MB"-> "1.2MB"
    number_part=s 
    for u in ("GB","MB","KB","B"):
        if s.endswith(u):
            unit=u
            number_part=s[:-len(u)] or 0 # "1.2MB" -> "1.2", mert a végéről levágjuk az mb hosszát, ami 2 B-nél 1 lenne
            break
    value=float(number_part)
    return int (value*SIZE_MULTIPLIERS[unit])
    
def file_sorted_by_size_desc(data):
    return sorted(data,key=lambda f:parse_size_to_bytes(f["size"]), reverse=True)

# =========================
# 2.5 Verziók 
# =========================

#versions = ["1.2.0", "1.10.0", "1.2.11", "2.0.0", "1.2.3"]

def parse_version(v):
    parts=v.split(".")
    major=int(parts[0]) if len(parts)>0 else 0
    minor=int(parts[1]) if len(parts)>0 else 0
    patch=int(parts[2]) if len(parts)>0 else 0
    return (major,minor,patch)

def version_sorted(data):
    return sorted(data,key=parse_version)

def newest_version(data):
    return max(data,key=parse_version)

# =========================
# 2.1 Tranzakciók 
# =========================
# {"id": "T100", "user": "u1", "amount": "-12000",
# "currency": "HUF", "ts": "2026-03-11T09:10:00"},
def amount_int(tx):
    return int(tx["amount"])

def tx_sort_key(tx):
    return(
        -abs(amount_int(tx)),
        -parse_ts_iso(tx["ts"]).timestamp(),
    )

def transactions_sorted(data):
    return sorted(data,key=tx_sort_key,reverse=False)

# =========================
# 3.4 IP rendezés
# =========================
#ips = ["10.0.0.2", "10.0.0.12", "192.168.1.1", "10.0.0.3", "172.16.0.5"]

#hasonló nagyon, mint a verziószám!!!

def ipv4_key(ip):
    a,b,c,d=ip.strip().split(".")
    return (int(a),int(b),int(c),int(d))
#szét kell bontani valahogy :)

def ips_sorted(data):
    return sorted(data,key=ipv4_key)

def max_ip(data):
    return max(data,key=ipv4_key)


# =========================
# 3.5 Tranzakciók user-összegzés 
# =========================
#user szerint csoportosítva!!!!!
def user_txt_summeries(data):
    data_sorted=sorted(data, key=lambda tx:tx["user"])
    summaries=[]
    for user,group in groupby(data_sorted,key=lambda tx: tx["user"]):
        txs=list(group)
        amounts=[amount_int(tx) for tx in txs]
        net=sum(amounts)
        debits=[a for a in amounts if a<0]
        biggest_debit=min(debits) if debits else 0
        summaries.append({
            "user": user,
            "count":len(txs),
            "net_amount":net,
            "biggest_debit":biggest_debit
        })
    return summaries

def top_users_by_abs_net(data,n=3):
    summaries=user_txt_summeries(data)
    return sorted(summaries,key=lambda s:abs(s["net_amount"]), reverse=True)[:n]

# =========================
# 2.2 Log riport rendezése
# =========================
def logs_report_sorted(data):
    return sorted(
        data,
        key= lambda l:(
            l["endpoint"],
            l["status"],
            -l["rt_ms"]
        )
    )


# =========================
# 3.6 Stabil rendezés több lépésben 
# =========================
def logs_sorted_stable_two_pass(data):
    first=sorted(data,key=lambda l:l["rt_ms"], reverse=True)
    return sorted(first,key=lambda l:l["endpoint"])



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

#dirty = [
#{"id": "A", "score": "10"},
#{"id": "B", "score": None},
#{"id": "C"},
#{"id": "D", "score": "2"},
#]

def dirty_sorted_by_score(data):
    #safe_int(value) -> int | None
    #safe_sorted ugyanaz mint a sorted fg., csak a key hibás értékek a végére kerülnek.
    def key(item):
        score=safe_int(item.get("score"))
        if score is None:
            raise ValueError("missing score")
        
        return score
    
    return safe_sorted(data,key=key)

# =========================
# 3.7 Jegyek + groupby – megoldás
# =========================
def grade(points):
    if points<=49:
        return 1
    if points<=59:
        return 2
    if points<=69:
        return 3
    if points<=84:
        return 4
    return 5

def results_sorted_by_grade(data):
    #jegy>pont>név ABC 
    return sorted(data,key=lambda r: (-grade(int(r["points"])), -int(r["points"]), r["name"]))

def grade_counts(data):
    data_sorted=sorted(data,key=lambda r:grade(int(r["points"])))    
    result={}
    for g,group in groupby(data_sorted,key=lambda r:grade(int(r["points"]))):
        result[g]=len(list(group))
    return result




# =========================
# 2.6 Case-insensitive rendezés – megoldás
# =========================

# =========================
# 2.7 Természetes rendezés ID-kre – megoldás
# =========================
#ticket_ids = ["ID1", "ID2", "ID10", "ID3", "ID21", "ID11"]
def netural_ticket_key(ticket_id):
    s=ticket_id.strip()
    prefix="".join(ch for ch in s if not ch.isdigit())
    #ID
    digits="".join(ch for ch in s if ch.isdigit())
    #1,2,10,3,21,11
    return (prefix, int(digits) if digits else 0)


def tickets_ids_sorted_natural(data):
    return sorted(data,key=netural_ticket_key)

def max_ticket_id(data):
    return max(data,key=netural_ticket_key)

# =========================
# 3.8 Napi endpoint riport – megoldás
# =========================


# =========================
# Demo futtatás
# =========================

if __name__ == "__main__":
    # Itt lehet meghívni a fenti függvényeket és kiírni az eredményeket teszteléshez
    print("== 1.1 Ranglista ==")
    for s in student_ranking(students):
        print(s["neptun"], s["name"],round(finals_points(s),2))

    print("== 1.3 Alerts rendezve ==")
    for a in alerts_sorted(alerts):
        print(a["id"], a["severity"],a["ts"],a["service"])
