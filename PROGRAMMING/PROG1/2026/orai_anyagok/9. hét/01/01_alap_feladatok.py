#Feladat 1

szamok=[3,8,11,14,20,21,24]
paros_szamok=[]

for szam in szamok:
    if szam%2==0:
        paros_szamok.append(szam)

print(paros_szamok)

#Feladat 2
nevek = ["Anna", "Lajos", "Éva", "Kristóf"]
hosszak = []

for nev in nevek: 
    hosszak.append(len(nev))
    
print(hosszak)

#Feladat 3
szamok=[45,120,87,230,15,180]
osszeg=0
for szam in szamok:
    if szam>100:
        osszeg+=szam
print(osszeg)

#Feladat 4 
szamok=[-2,5,0,3,-1,8]
darab=0

for szam in szamok:
    if szam>0:
        darab+=1
        
print(darab)

#Feladat 5
szamok=[12,7,25,3,18]
legkisebb=szamok[0]

for szam in szamok:
    if szam<legkisebb:
        legkisebb=szam
print(legkisebb)

#Feladat 6
szavak=["kutya","macska","ló","elefánt"]

for szo in szavak:
    if len(szo)>=5:
        print(szo)
        
#Feladat 7
szavak=["alma","körte","barack"]
osszes_karakter=0
for szo in szavak:
    osszes_karakter+=len(szo)      

#Feladat 8
szamok=[10,20,30,40,50,60]
eredmeny=[]

for index in range(len(szamok)):
    if index%2==0:
        eredmeny.append(szamok[index])
print(eredmeny)

#Feladat 9 
szavak=["alma","körte","banán","eper"]

for szo in szavak:
    if "a" in szo:
        print(szo)
        
#Feladat 10
szamok=[10,50,30,50,20]
legnagyobb=szamok[0]
legnagyobb_index=0

for index in range(len(szamok)):
    if szamok[index]>legnagyobb:
        legnagyobb=szamok[index]
        legnagyobb_index=index
print(legnagyobb_index)