def ellenorzes_ket_modon(number_value):
    first_result=False
    second_result=False
    
    if number_value==3 or number_value ==4:
        first_result=True
    else:
        first_result=False
        
    if number_value in (3,4):
        second_result=True
    else:
        second_result=False
    
    return first_result,second_result

#Miért "rossz"?
#Túl hosszú a változók nevei, miközben a logika egyszerű
#Felesleges else ág -> felesleges if, közvetlen visszaadhatók az értékek