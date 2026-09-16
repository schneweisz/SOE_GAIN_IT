#41
szamok = [1, 2, 3, 4, 5]
#(x, x**2)
eredmeny = [(szam, szam*2)for szam in szamok]
print(eredmeny)

#42
szavak = ["alma", "körte", "banán"]
maganhangzok = 'aáeéiíoóöőüúű'
szotar = {}
# dict comprehension
szotarka = {szo: sum(1 for karakter in szo.lower() if karakter in maganhangzok) for szo in szavak}
#general
for szo in szavak:
    for betu in szo:
        magan = 0
        if betu in 'maganhangzok':
            magan += 1
            szotar[szo] = magan
        else:
            continue
print(szotar)
print (szotarka)


#43
szamok = [1, 2, 3, 4, 5, 6]
eredmeny = {"páros":[szam for szam in szamok if szam%2==0],
            "páratlan":[szam for szam in szamok if szam%2!=0]}
print(eredmeny)

#44
szavak = ["alma", "körte", "eper", "szilva"]
leghosszabb = max(szavak, key=len) # key = mi alapján rendezze sorba
print(leghosszabb)

#45
#--------------------------------------

#46
logok = [
    "INFO: elindult",
    "ERROR: hiba történt",
    "INFO: fut",
    "WARNING: kevés memória",
    "ERROR: összeomlott"
]
info_db = sum(1 for sor in logok if sor.startswith("INFO"))
error_db = sum(1 for sor in logok if sor.startswith("ERROR"))
error_sorok = [sor for sor in logok if sor.startswith("ERROR")]

print(info_db, error_db, error_sorok)

#47
#--------------------------------------
#48
#--------------------------------------

#49
szorzotabla = [[sor*oszlop for oszlop in range(1,11)] for sor in range(1,11)]
for sor in szorzotabla:
    print(sor)

#50
szamok = [4, 11, 16, 23, 8, 42, 7, 10]

#ciklusos
kivalasztottak_ciklus = []
for szam in szamok:
    if szam>10 and szam%2==0:
        kivalasztottak_ciklus.append(szam)
osszeg_ciklus=sum(kivalasztottak_ciklus)

print(kivalasztottak_ciklus)

#comp
kivalasztottak_comp = [szam for szam in szamok if szam>10 and szam%2==0]
osszeg_comp=sum(kivalasztottak_comp)

print(kivalasztottak_comp)