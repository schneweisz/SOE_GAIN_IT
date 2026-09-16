scores = [56, 72, 89, 45, 90, 100, 67]


def sikeresek_rosszul(values):
   #az erdeti listát módosítja!!! (nem várt mellékhatás) 
    i = 0
    while i < len(values):
        if values[i] < 50:
            values.pop(i)
        else:
            i += 1
    return values


if __name__ == "__main__":
    data = scores
    print("Előtte:", data)
    print("Eredmény:", sikeresek_rosszul(data))
    print("Utána (eredeti is változott):", data)
