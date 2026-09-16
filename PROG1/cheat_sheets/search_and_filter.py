from base import data_list

# Find one specific item by name
def find_by_name(target_name):
    for item in data_list:
        if item.name.lower() == target_name.lower():
            return item
    return None

# Get a list of items above a certain score
def filter_above(threshold):
    result = []
    for item in data_list:
        if item.value >= threshold:
            result.append(item)
    return result