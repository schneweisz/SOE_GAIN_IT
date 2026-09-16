def grade_from_points(points):
    if points< 0:
        return "hibas"
    #innentől biztosan tudjuk hogy 0 feletti az érték vagy 0.
    if points<=49:
        return "elégtelen"
    if points<=69:
        return "közepes"
    if points<=84:
        return "jó"
    if points<=100:
        return "jeles"
    
    return "hibas"

mintak={-5,0,49,50,69,70,84,100,101}

for point in mintak:
    print(f"{point} -> {grade_from_points(point)}")