#pontszámok alapján el kell dönteni hányast kap a hallgató

def grade_from_points(points):
    result_text=""
    
    if points<0:
        result_text="hibas"
    else:
        if points<=49:
            result_text="elégtelen"
        else:
            if points<=69:
                result_text="közepes"
            else:
                if points<=84:
                    result_text="jó"
                else:
                    if points<=100:
                        result_text="jeles"
                    else:
                        result_text="hibas"
    return result_text
 #mi a hiba?
 #túl mélyen egymásba ágyazott if-else szerkezet-> nehezebb követni
 #hosszabb a kód, mint szükségesebb lenne
 #kevésbé olvashatóbb mint a "lapos", visszatérési értékes verzió