def sorting(item):
    return(-item[1], item[0])


def second(text):
    text = text.lower()

    cleaned = ""

    for char in text:
        if char.isalpha():
            cleaned += char
        else:
            cleaned += " "

    words = cleaned.split()

    stats = {}

    for word in words:
        stats[word] = stats.get(word, 0) + 1
    
    sorted_words = sorted(stats.items(), key=sorting)

    for word, count in sorted_words[:5]:
        print(word, count)
    


if __name__ == "__main__":
  
    input_text = "Alma, körte, alma! Sárga körte; alma? Banán."

    second(input_text)

    # 1

    # 2

    # 3

    # 4