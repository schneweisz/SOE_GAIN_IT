#file olvasva megnézzük a szavak számát
def szavak_szamlalasa():
    #manuálisan nyitunk és zárunk
    f=open("szöveg.txt","r")
    #with open
    try:
        szoveg=f.read()
    except:
        szoveg=""
        #ha hiba van nem zárodik be
    f.close()
    
    szavak=szoveg.split()
    szamlalas=len(szavak)
    
    print(f"Szavak száma:{szamlalas}")


try:
    szavak_szamlalasa()
except:
    print("hiba")