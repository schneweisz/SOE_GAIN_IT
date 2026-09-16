from base import Entity, data_list

# --- TXT FILE EXAMPLE (data.txt) ---
# Name;Score;Category
# Alice;85;Math
# Bob;42;Physics
# ----------------------------------

def load_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # next(f) # Uncomment this line if the file has a header (first line)
            for line in f:
                if line.strip():
                    # Split by semicolon (change ';' to ',' if CSV)
                    parts = line.strip().split(';')
                    # Create object and add to global list
                    new_item = Entity(parts[0], parts[1], parts[2])
                    data_list.append(new_item)
        print(f"Successfully loaded {len(data_list)} items.")
    except FileNotFoundError:
        print("Error: File not found!")

def save_to_file(filename, filtered_list):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in filtered_list:
            f.write(f"{item.name};{item.value};{item.category}\n")

# Usage: load_from_file('data.txt')