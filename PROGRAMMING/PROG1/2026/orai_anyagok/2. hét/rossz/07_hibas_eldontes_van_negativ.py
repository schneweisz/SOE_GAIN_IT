def has_negative(number_list):
    found=False
    for number_item in number_list:
        if number_item<0:
            found=True
        else:
            found=found
    return found

#értelmetlen else ág
#az első talált után nem lép ki