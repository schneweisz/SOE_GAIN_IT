def gyakorisag_szamol(lista):
    stat={}
    
    for elem in lista:
        if elem in stat:
            stat[elem]+=1
        else:
            stat[elem]=1
    return stat

adatok=["piros","kek","piros","zold","kek","piros"]
eredmeny=gyakorisag_szamol(adatok)
for kulcs in eredmeny:
    print(f"-{kulcs}: {eredmeny[kulcs]}")