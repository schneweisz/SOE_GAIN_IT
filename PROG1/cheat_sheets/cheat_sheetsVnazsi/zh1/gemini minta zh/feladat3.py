
def adatcsoportositas(adatok:str):
    """
    Feldolgozza a bemeneti stringet, elvégzi az adattisztítást a README alapján,
    és egy szótárba csoportosítja a játékosok érvényes eseményeit.
    """
    sorok = adatok.strip().split("\n")
    userek = {}
    for sor in sorok:
        tiszta_sor = sor.strip()
        if not tiszta_sor: # Átugorja az üres sorokat
            continue

        reszek = tiszta_sor.split(";")
        if len(reszek) != 4: # Biztosítja, hogy a sor 4 részből álljon
            continue

        timestamp, player, event, value = reszek

        # Adattisztítási szabályok
        if event not in ["LOGIN","MATCH","SCORE","CRASH"]:
            continue
        
        # A README szerint a SCORE csak akkor érvényes, ha a value POZITÍV egész szám.
        # Ezt egy try-except blokkal biztonságos ellenőrizni.
        if event == "SCORE":
            try:
                pont = int(value)
                if pont <= 0: # Ha a pontszám nem pozitív, a rekord érvénytelen.
                    continue
            except ValueError: # Ha a value nem alakítható számmá (pl. '-'), a rekord érvénytelen.
                continue

        if player not in userek:
            userek[player] = []

        userek[player].append({
            "timestamp" : timestamp,
            "event" : event,
            "value" : value
        })
    # A return utasításnak a cikluson kívül kell lennie!
    return userek

def gyakorisag(userek:dict):
    login_db = 0
    match_db = 0
    score_db = 0
    crash_db = 0
    for event in userek.values():
        for item in event:
            if item['event'] == "LOGIN":
                login_db += 1
            elif item['event'] == "MATCH":
                match_db += 1
            elif item['event'] == "SCORE":
                score_db += 1
            elif item['event'] == "CRASH":
                crash_db += 1
    return{
        "LOGIN" : login_db,
        "MATCH" : match_db,
        "SCORE" : score_db,
        "CRASH" : crash_db
    }

def pontszam_statisztika(jatekosok: dict) -> list:
    """3/B: Kiszámolja a játékosok összpontszámát és visszaadja a Top 2-t."""
    pontok = {}
    for player, esemenyek in jatekosok.items():
        total_score = 0
        for esemeny in esemenyek:
            if esemeny['event'] == 'SCORE':
                # Az adatcsoportosítás már biztosította, hogy a value érvényes szám
                total_score += int(esemeny['value'])
        # Csak azokat a játékosokat vesszük figyelembe, akik szereztek pontot
        if total_score > 0:
            pontok[player] = total_score

    # Rendezés: elsődlegesen pontszám (csökkenő), másodlagosan név (növekvő)
    rendezett_jatekosok = sorted(pontok.items(), key=lambda item: (-item[1], item[0]))

    # Visszaadjuk a Top 2 játékost
    return rendezett_jatekosok[:2]

def crash_statisztika(jatekosok:dict):
    """3/C: Kiszámolja a szakadási arányt és megkeresi a legproblémásabb játékost."""
    ossz_event = 0
    ossz_crash = 0
    crashelt_jatekosok = {}
    for jatekos,adatok in jatekosok.items():
        crashelt_jatekosok[jatekos] = 0
        for event in adatok:
            ossz_event += 1
            if event['event'] == "CRASH":
                ossz_crash += 1
                crashelt_jatekosok[jatekos] += 1
    rendezett_crashek = sorted(crashelt_jatekosok.items(), key=lambda x: (-x[1],x[0]))
    return (ossz_crash / ossz_event) * 100, rendezett_crashek[0]

def riport(jatekosok:dict):
    riport_szotar = {}
    for jatekos, eventek in jatekosok.items():
        total_score = 0
        crash_db = 0
        match_halmaz = set()
        for event in eventek:
            if event['event'] == "SCORE":
                total_score += int(event['value'])
            elif event['event'] == "CRASH":
                crash_db += 1
            elif event['event'] == "MATCH":
                match_halmaz.add(event['value'])
        riport_szotar[jatekos] = {
            "match_egyedi_db" : len(match_halmaz),
            "total_score" : total_score,
            "crash_db" : crash_db
        }
    return riport_szotar

def elso_crash(jatekosok:dict):
    crashek_idoponttal = []
    for jatekos,eventek in jatekosok.items():
        for event in eventek:
            if event['event'] == "CRASH":
                crashek_idoponttal.append((event['timestamp'],jatekos))

    if crashek_idoponttal:
        legkorabbi_crash = min(crashek_idoponttal)
        return legkorabbi_crash
    return None    


if __name__ == "__main__":
    adatok="""
    2026-04-10 15:00;alex;LOGIN;-
    2026-04-10 15:01;alex;MATCH;arena-1
    2026-04-10 15:02;bob;MATCH;arena-1
    2026-04-10 15:03;alex;SCORE;500
    2026-04-10 15:04;bob;SCORE;300
    2026-04-10 15:05;bob;CRASH;lag
    2026-04-10 15:06;chloe;MATCH;arena-2
    2026-04-10 15:07;chloe;SCORE;750
    2026-04-10 15:08;chloe;SCORE;-10
    """
    
    # Adatok beolvasása, szűrése és a "Mester Szótár" felépítése
    jatekosok = adatcsoportositas(adatok)
    
    # 3/A
    print("--- 3/A Feladat ---")
    akciok_szama = gyakorisag(jatekosok)
    for kulcs, ertek in akciok_szama.items():
        print(f"{kulcs}={ertek}")
    print("-" * 50)
    
    # 3/B
    print("--- 3/B Feladat ---")
    top_jatekosok = pontszam_statisztika(jatekosok)
    for nev, pont in top_jatekosok:
        print(f"{nev} {pont}")
    print("-" * 50)

    # 3/C
    print("--- 3/C Feladat ---")
    arany, problemas = crash_statisztika(jatekosok)
    print(f"crash_arany={arany:.2f}%")
    print(f"problemas_player={problemas[0]} ({problemas[1]} crash)")
    print("-" * 50)

    # 3/D
    print("--- 3/D Feladat ---")
    teljes_riport = riport(jatekosok)
    for nev, adatok_dict in sorted(teljes_riport.items()):
        print(f"{nev} match_egyedi_db={adatok_dict['match_egyedi_db']} total_score={adatok_dict['total_score']} crash_db={adatok_dict['crash_db']}")
    print("-" * 50)

    # 3/E
    print("--- 3/E Feladat ---")
    elso = elso_crash(jatekosok)
    if elso:
        print(f"elso_crash_player={elso}")