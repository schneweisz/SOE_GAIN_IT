data_list=[12,-4,0,7,15,-2,8]
#összegzés: pozitivak, tiznél nagyobbak
sum_positive=0
sum_bigger_than_ten=0

for current_number in data_list:
    if current_number>0:
        sum_positive+=current_number
    
    if current_number>10:
        sum_bigger_than_ten+=current_number

print("pozitiv:",sum_positive)
print("10nél nagyobb:",sum_bigger_than_ten)
