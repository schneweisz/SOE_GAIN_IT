def find_max_index(input_list):
    if not input_list:
        return -1
    max_idx=0
    max_value=input_list[0]
    for i in range(1,len(input_list)):
        if input_list[i]>max_value:
            max_value=input_list[i]
            max_idx=i  
    return max_idx

tesztek=[
    [],
    [5],
    [3,7,2,7,1],
    [-4,-2,-9]
]

for t in tesztek:
    idx=find_max_index(t)
    print (f"lista={t} -> max index: {idx}")