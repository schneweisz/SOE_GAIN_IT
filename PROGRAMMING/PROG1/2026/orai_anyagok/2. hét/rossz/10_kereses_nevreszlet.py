name_list=["Anna","Bela","Csaba","Dora","Emese"]
what_to_find="sa"

result_index=-1
i=0
while i<len(name_list):
    if what_to_find.lower() in name_list[i].lower():
        result_index=i
        break
    i=i+1
    
#while nem optimális ide
#result_index változó felesleges
#what_to_findre többször meghivjuk a lower függvényt.