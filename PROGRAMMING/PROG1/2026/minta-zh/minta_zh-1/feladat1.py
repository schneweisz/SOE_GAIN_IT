def cikkelemzes(sorok):
    adatok={}
    for sor in sorok:
        if ';' in sor:
            user, slug = sor.strip().split(';')
            if user not in adatok:
                adatok[user] = set()
            adatok[user].add(slug)
        else:
            break

    u1,u2 = sorok[-1].strip().split()
    cikkek1 = adatok.get(u1, set())
    cikkek2 = adatok.get(u2, set())
    c = cikkek1 & cikkek2
    union = cikkek1 | cikkek2
    return len(cikkek1), len(cikkek2), len(c), len(union)


if __name__ == "__main__":
    sorok = [
    "anna;python-alapok",
    "anna;dict-es-set",
    "anna;python-alapok",
    "bela;python-alapok",
    "bela;fajlkezeles",
    "cili;dict-es-set",
    "VEGE",
    "anna bela"
    ]
    
    u1_db, u2_db, kozos_db, all_db = cikkelemzes(sorok)
    print(f"u1_egyedi_db={u1_db}")
    print(f"u2_egyedi_db={u2_db}")
    print(f"kozos_db={kozos_db}")
    print(f"osszes_db={all_db}")
