input_data=["piros","kek","piros","zold","kek","piros"]
stats={}

for item in input_data:
    if item in stats.keys():
        old_value=stats[item]
        new_value=old_value+1
        stats[item]=new_value
    else:
        stats[item]=1
        
print("bemenet: ",input_data)
for k in stats:
    print (k,"=", stats[k])

#kézzel ellenőrzi a kulcsot ami körülményes!
#nincs függvényben.