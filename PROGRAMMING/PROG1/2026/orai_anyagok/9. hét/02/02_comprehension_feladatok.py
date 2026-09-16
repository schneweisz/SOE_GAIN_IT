#11
szamok = [i*i for i in range (1,21)]
print(szamok)

#12
szamok = [2, 5, 8, 11, 14]
paros_szamok=[szam*szam for szam in szamok if szam%2==0]
print(paros_szamok)

#13
szavak = ["alma", "körte", "banán"]
nagybetus = [szo.upper() for szo in szavak]
print(nagybetus)

#14
szavak = ["alma", "körte", "barack"]
szavak5 = [szo for szo in szavak if len(szo)>5]
print(szavak5)

#15
szamok = [1, 2, 3, 4, 5]
parosparatlan = [f"{szam}. páros" if szam%2==0 else f"{szam}. páratlan" for szam in szamok]
print(parosparatlan)

#16
szavak = ["alma", "körte", "eper"]
szavakhossza = [len(szo) for szo in szavak]
print(szavakhossza)

#17
szavak = ["alma", "körte", "eper"]
szotar = {szo:szo[0] for szo in szavak}
print(szotar)

#18
szotar = {"a": 1, "b": 5, "c": 10}
ujszotar = {key:value for key,value in szotar.items() if value>3}
print(ujszotar)

#19
szavak = ["alma", "autó", "ablak", "banán"]
szotar = {szo[0] for szo in szavak}
print(szotar)

#20
szamok = [1, 2, 2, 3, 4, 4, 5]
egyedi = [szam for szam in szamok if szam%5==2]