def tisztitas(adatok:str):
    sorok = adatok.strip().split("\n")
    esemenynaplo = {}
    userek = sorok[-1].strip().split()
    u1 = userek[0]
    u2 = userek[1]
    for sor in sorok:
        tiszta_sor = sor.strip()
        if not tiszta_sor:
            continue
        if tiszta_sor == "VEGE":
            break
        
        if ";" in tiszta_sor:
            adat = tiszta_sor.split(";")
            user = adat[0]
            video_id = adat[1]
            if user not in esemenynaplo:
                esemenynaplo[user] = set()
            esemenynaplo[user].add(video_id)
    return esemenynaplo, u1, u2

def elemzes(szotar:dict, user1, user2):
    set1 = szotar.get(user1, set())
    set2 = szotar.get(user2,  set())
    return len(set1), len(set2), len(set1 & set2), len(set1 | set2)



if __name__ == "__main__":
    adtok = """
    nora;vid-101
    nora;vid-102
    nora;vid-101

    tibi;vid-102
    tibi;vid-201

    dori;vid-999
    VEGE

    nora tibi
    """
    szotar, user1, user2 = tisztitas(adtok)
    #print(szotar)

    user1_db, user2_db, kozos, osszes = elemzes(szotar, user1, user2)
    print(f"u1_egyedi_db={user1_db}")
    print(f"u2_egyedi_db={user2_db}")
    print(f"kozos_db={kozos}")
    print(f"osszes_db={osszes}")    