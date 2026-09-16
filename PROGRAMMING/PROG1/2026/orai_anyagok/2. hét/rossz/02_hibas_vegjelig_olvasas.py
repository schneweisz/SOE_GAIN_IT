#végjelig beolvasunk számokat
#kiírjuk: a pozitív számok összegét, a páros számok darabszámát, és hány jó szám volt

sum_of_positive_numbers=0
count_even_numbers=0
count_all_ok_numbers=0

running_flag=True

while running_flag:
    raw_text=input("Szám: ")
    raw_text=raw_text.strip()
    
    try:
        number_now=int(raw_text)
    except:
        print("Nem jó szám")
        continue
    
    if number_now==0:
        running_flag=False
    else:
        count_all_ok_numbers=count_all_ok_numbers+1
        
        if number_now>0:
            sum_of_positive_numbers=sum_of_positive_numbers+number_now
        
        if number_now%2==0:
            count_even_numbers=count_even_numbers+1
    