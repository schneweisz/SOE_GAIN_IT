def szavak_szamlalasa(fajl_nev):
    try:
        with open(fajl_nev,"r",encoding="utf-8") as f
            szoveg=f.read()
        szavak=szoveg.split()
        return len(szavak)
    except FileNotFoundError:
        print (f"Hiba: file nem található")
    except UnicodeDecodeError:
        print (f"
               file hibás kódolás")