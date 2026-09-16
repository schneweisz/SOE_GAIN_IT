
from matplotlib import use
from urllib3 import Retry


def adatcsoportositas(adatok:str):
    #a hosszu stringet atalakitom egy osszetett szotarra
    sorok = adatok.split("\n")
    userek = {}
    for sor in sorok:
        tiszta_sor = sor.strip()
        if not tiszta_sor:
            continue
        reszek = tiszta_sor.split(";")
        ido,nev,akcio,ertek = reszek
        
        # --- KÖTELEZŐ ADATTISZTÍTÁS ---
        if akcio not in ["LOGIN", "VIEW", "BUY", "ERROR"]:
            continue
        if akcio == "BUY" and int(ertek) <= 0:
            continue
            
        # --- FELHASZNÁLÓ LISTÁJÁNAK LÉTREHOZÁSA ---
        if nev not in userek:
            userek[nev] = []
            
        # --- AKCIÓ HOZZÁFŰZÉSE A FELHASZNÁLÓHOZ ---
        userek[nev].append({
            "ido": ido,
            "akcio": akcio,
            "ertek": ertek
        })
    return userek

def szamol_akciok(userek:dict):
    login_db = 0
    view_db = 0
    buy_db = 0
    error_db = 0
    for akcio in userek.values():
        for item in akcio:
            if item['akcio'] == "LOGIN":
                login_db += 1
            elif item['akcio'] == "VIEW":
                view_db += 1
            elif item['akcio'] == "BUY":
                buy_db += 1
            elif item['akcio'] == "ERROR":
                error_db += 1
    return{
        "LOGIN" : login_db,
        "VIEW" : view_db,
        "BUY" : buy_db,
        "ERROR" : error_db
    }

def koltesek(userek:dict):
    user_koltesek = {}
    for nev, akcio_lista in userek.items():
        osszeg = 0
        for akcio in akcio_lista:
            if akcio['akcio'] == "BUY":
                # Az értéket számmá alakítjuk, és az összeghez adjuk
                osszeg += int(akcio['ertek'])
                
        # Amikor a belső ciklus végzett, elmentjük a user végső összegét
        user_koltesek[nev] = osszeg
        
    # Rendezzük érték szerint csökkenő (-x[1]), és név szerint növekvő (x[0]) sorrendbe.
    # A [:2] szeletelés a sorted() lefutása után, az eredmény listán történik.
    return sorted(user_koltesek.items(), key=lambda x: (-x[1], x[0]))[:2]
        
def errorarany(userek:dict):
    #hibas rekordok aranya az osszeshez kepest
    
    ossz_akcio = 0
    ossz_hibas = 0
    user_hibak = {}
    for nev,akcio_lista in userek.items():
        # Idézőjelek nélkül használjuk a 'nev' változót!
        user_hibak[nev] = 0
        for akcio in akcio_lista:
            ossz_akcio += 1
            if akcio['akcio'] == "ERROR":
                ossz_hibas += 1
                user_hibak[nev] += 1
    # A legtöbb hibát vétő user megkeresése (csökkenő hiba, növekvő név)
    rendezett_hibak = sorted(user_hibak.items(), key=lambda x: (-x[1], x[0]))
    return (ossz_hibas / ossz_akcio) * 100, rendezett_hibak[0]

def riport(userek:dict):
    report = {}
    for nev, akcio_lista in userek.items():
        latott_cikkek = set()
        osszes_koltes = 0
        hibak_szama = 0
        for akcio in akcio_lista:
            if akcio['akcio'] == "VIEW":
                latott_cikkek.add(akcio['ertek'])     
            elif akcio['akcio'] == "BUY":
                osszes_koltes += int(akcio['ertek'])
            elif akcio['akcio'] == "ERROR":
                hibak_szama += 1
        # A tuple helyett egy belső szótárat mentünk el, ami sokkal olvashatóbb.
        # A len(latott_cikkek) már itt kiszámolja a darabszámot.
        report[nev] = {
            "view_egyedi_db": len(latott_cikkek),
            "koltes": osszes_koltes,
            "error_db": hibak_szama
        }
    return report

def elso_hiba(userek:dict):
    hibak_idoponttal = []
    for nev, akcio_lista in userek.items():
        for akcio in akcio_lista:
            if akcio['akcio'] == "ERROR":
                # Egy tuple-t fűzünk a listához: (idő, név)
                hibak_idoponttal.append((akcio['ido'], nev))
    
    # Ha van hiba a listában, a min() megkeresi a legkisebb időpontot
    if hibak_idoponttal:
        legkorabbi_hiba = min(hibak_idoponttal)
        return legkorabbi_hiba[1]  # A tuple-ből csak a nevet adjuk vissza
    return None

# Főprogram
if __name__ == "__main__":
    adatok="""
    2026-03-21 10:00;anna;LOGIN;-
    2026-03-21 10:01;anna;VIEW;python-alapok
    2026-03-21 10:02;bela;VIEW;python-alapok
    2026-03-21 10:03;anna;BUY;1200
    2026-03-21 10:04;bela;BUY;800
    2026-03-21 10:05;bela;ERROR;timeout
    2026-03-21 10:06;cili;VIEW;dict-es-set
    2026-03-21 10:07;cili;BUY;1000
    2026-03-21 10:08;cili;BUY;-5

    """
    userek = adatcsoportositas(adatok)
    
    # 3/A
    akciok_szama = szamol_akciok(userek)
    for kulcs, ertek in akciok_szama.items():
        print(f"{kulcs}={ertek}")
    print("-"*50)
    
    # 3/B
    top_vasarlok = koltesek(userek)
    for nev, osszeg in top_vasarlok:
        print(f"{nev} {osszeg}")
    print("-"*50)

    
    # 3/C
    arany,problemas = errorarany(userek)
    print(f"hibaarany={arany:.2f}%")
    print(f"problemas_user={problemas[0]} ({problemas[1]} error)")
    print("-"*50)


    # 3/D
    teljes_riport = riport(userek)
    # A .items() listáját a sorted() alapból a kulcs (név) szerint rendezi.
    for nev, adatok in sorted(teljes_riport.items()):
        print(f"{nev} view_egyedi_db={adatok['view_egyedi_db']} koltes={adatok['koltes']} error_db={adatok['error_db']}")

    # 3/E
    print("-" * 50)
    elso_error = elso_hiba(userek)
    if elso_error:
        print(f"elso_error_user={elso_error}")
