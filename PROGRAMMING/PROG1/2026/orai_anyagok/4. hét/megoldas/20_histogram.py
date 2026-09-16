scores = [56, 72, 89, 45, 90, 100, 67, 72, 38, 84, 91, 60, 73, 88, 55, 49]


def histogram_rosszul(values):
    bins = {"0-49": 0, "50-59": 0, "60-69": 0, "70-79": 0, "80-89": 0, "90-100": 0}
    for s in values:
        if s < 50:  
            bins["0-49"] += 1
        elif s < 60:  
            bins["50-59"] += 1
        elif s < 70:
            bins["60-69"] += 1
        elif s < 80:
            bins["70-79"] += 1
        elif s < 90:  
            bins["80-89"] += 1
        else:
            bins["90-100"] += 1
    return bins


if __name__ == "__main__":
    h = histogram_rosszul(scores)
    for k in ["0-49", "50-59", "60-69", "70-79", "80-89", "90-100"]:
        print(f"{k}: {h[k]}")
