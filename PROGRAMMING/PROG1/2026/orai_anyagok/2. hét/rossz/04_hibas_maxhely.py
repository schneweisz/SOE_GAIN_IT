def find_max_index(input_list):
    if len(input_list)==0:
        return -1
    
    max_idx_value=0
    max_num_value=input_list[0]
    index_now=1
    
    while index_now<len(input_list):
        if input_list[index_now]>max_num_value:
            max_num_value=input_list[index_now]
            max_idx_value=index_now
        index_now=index_now+1
    return max_idx_value
#indokolatlan 'while'-os indexelés, egyszerűbb a for-ral
