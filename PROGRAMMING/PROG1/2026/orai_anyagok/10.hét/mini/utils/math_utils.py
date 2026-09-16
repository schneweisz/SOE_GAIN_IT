"""
Egyszerű matematikai segédfüggvények.

Ez a modul alapműveleteket tartalmaz(összeadás,kivonás,szorzós,osztás)
Az osztás 0-val történő kísérlete esetén a függvény None értéket ad vissza
"""
def add(a,b):
    # help(utils.math_utils.add)
    """
        Két számot összegét adja vissza
        
        Paraméterek:
            a (int): első szám
            b (int): második szám
        
        Visszatér:
            int: összeg
    """
    return a+b

def average(a,b):
    #help(utils.math_utils.average)
    """
        Két számot átlagát adja vissza

        Paraméterek:
            a (int): első szám
            b (int): második szám

        Visszatér:
            int: átlag
    """
    return (a+b)/2 

#subtract
def subtract(a,b):
    """
        Két szám külöbségét adja visza
            Paraméterek:
                a (int): első szám (kisebbítendő)
                b (int): második szám (kivonandó)
            Visszatér:
                a-b (int) különbsége
    """
    return a-b
#multiply

def multiply(a,b):
    """ 
        Két szám szorzatát adja vissza
            Paraméterek:
                a (int): első szám
                b (int): második szám
            Visszatér:
                a és b (int) szorzata
    """
    return a-b
#divide (0-val lehet-e osztani?)

def divide(a,b):
    """
        Két szám osztása
           Paraméterek:
                a (int): osztandó
                b (int): osztó
            Visszatér:
               Az osztás eredménye (int), vagy "None", ha b==0
    """
    if b==0:
        return None
    return a/b

#python3 -c "import utils.math_utils; help(utils.math_utils)" 