def first_result_index(names,what_to_find):
    what_to_find=what_to_find.lower()
    for i in range(len(names)):
        if what_to_find in names[i].lower:
            return i
    return -1


name_list=["Anna","Bela","Csaba","Dora","Emese"]
what_to_find="sa"
idx=first_result_index(name_list,what_to_find)


#while nem optimális ide
#result_index változó felesleges
#what_to_findre többször meghivjuk a lower függvényt.