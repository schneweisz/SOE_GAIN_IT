from base import data_list

def get_category_stats():
    # counts: how many items in a category
    # sums: total value in a category
    counts = {}
    sums = {}

    for item in data_list:
        cat = item.category
        if cat not in counts:
            counts[cat] = 1
            sums[cat] = item.value
        else:
            counts[cat] += 1
            sums[cat] += item.value

    # Printing category averages
    for cat in counts:
        avg = sums[cat] / counts[cat]
        print(f"Category {cat}: Average = {avg:.2f}, Count = {counts[cat]}")

# Usage: get_category_stats()