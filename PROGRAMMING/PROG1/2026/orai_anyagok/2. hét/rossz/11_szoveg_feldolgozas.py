# kapott szövegből 3 részeredmény
#  1. melyik a leghosszabb szó
#  2. hány szóból áll
#  3. hány szóköz van benne

#1 függvény csak 1 feladatot hajtson végre
# felesleges range használat, mivel a string alapból iterálható
#a feltételek sokszor feleslegesen ismétlődnek
#hosszú beágyazott if szerkezet
def feldolgozas_hosszu(szoveg):
    #rossz megközelités: kézzel iterálunk, feleslegesen.
    #kitöröljük a szóközöket, nagybetűvé alakítjuk a kicsiket, számokat nem piszkáljuk!
    nagyobb = ""
    for i in range(len(szoveg)):
        if szoveg[i] != " ":
            if szoveg[i].isalpha():
                nagyobb += szoveg[i].upper()
            else:
                if szoveg[i].isdigit():
                    nagyobb += szoveg[i]
    #szóközök számlálásra nehéz módon
    szokozok = 0
    for i in range(len(szoveg)):
        if szoveg[i] == " ":
            szokozok += 1
    #szavak szétválasztása nehéz módon (split)
    szavak = ""
    for c in szoveg:
        if c == " ":
            szavak += "|"
        else:
            szavak += c
 
    return nagyobb, szokozok, szavak
 
 
s1 = "Hello World 123"
s2 = "Python3 programozas!"
 
print("Hosszú verzió s1:")
print(feldolgozas_hosszu(s1))
print("\nHosszú verzió s2:")
print(feldolgozas_hosszu(s2))
 