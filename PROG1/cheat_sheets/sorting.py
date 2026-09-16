from base import data_list

# 1. MIN (Lowest value)
def get_min():
    if not data_list: return None
    min_item = data_list[0]
    for item in data_list:
        if item.value < min_item.value:
            min_item = item
    return min_item

# 2. MAX (Highest value)
def get_max():
    if not data_list: return None
    max_item = data_list[0]
    for item in data_list:
        if item.value > max_item.value:
            max_item = item
    return max_item

# 3. TOP 5 (Sorting descending)
def get_top_5():
    # Helper function for sorting (key)
    def sort_key(obj): return obj.value
    
    # Sorts the original list descending
    data_list.sort(key=sort_key, reverse=True)
    return data_list[:5]

# 4. AVERAGE (Math)
def get_average():
    if not data_list: return 0
    total = 0
    for item in data_list:
        total += item.value
    return total / len(data_list)