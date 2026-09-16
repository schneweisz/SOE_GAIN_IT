print("Feladat 1")
szamok = [3, 8, 11, 14, 20, 21, 24]
paros_szamok=[szam for szam in szamok if szam%2==0]
print(paros_szamok)

print("Feladat 2")
nevek = ["Anna", "Lajos", "Éva", "Kristóf"]
hosszak=[len(nev) for nev in nevek]
print(hosszak)

#sum()
print("Feladat 3")
szamok = [45, 120, 87, 230, 15, 180]
osszeg=sum([szam for szam in szamok if szam>100])
print(osszeg)

print("Feladat 4")
szamok = [-2, 5, 0, 3, -1, 8]
#len
darab=len([szam for szam in szamok if szam>0])
print(darab)

print("Feladat 5")
szamok = [12, 7, 25, 3, 18]
legkisebb=min(szamok)
#ez a feladat comprehensionnel nem oldható meg egyszerűen
print(legkisebb)

print("Feladat 6")
szavak = ["kutya", "macska", "ló", "elefánt"]
hosszu_szavak=[szo for szo in szavak if len(szo)>=5]
for szo in hosszu_szavak:
    print(szo)
    
print("Feladat 7")
szavak = ["alma", "körte", "barack"]
osszes_karakter=sum([len(szo) for szo in szavak])
print(osszes_karakter)

print("Feladat 8")
szamok = [10, 20, 30, 40, 50, 60]
eredmeny=szamok[::2]
print(eredmeny)

print("Feladat 9")
szavak = ["alma", "körte", "banán", "eper"]
a_betus_szavak=[szo for szo in szavak if "a" in szo]

for szo in a_betus_szavak:
    print(szo)
    
print("Feladat 10")
szamok = [10, 50, 30, 50, 20]
legnagyobb_index=szamok.index(max(szamok))
print(legnagyobb_index)