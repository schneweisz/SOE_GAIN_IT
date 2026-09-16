"""
    Szöveges (string) segédfüggvények

    Ebben a modulban egyszerű szövegmanipuláló függvények találhatók
"""

def shout(text):#full nagybetű
    """
    Nagybetűssé alakítja a kapott szöveget.

    Paraméterek:
        text(string): Bemeneti szöveg.
    
    Visszatér:
        A szöveg nagybetűs változata
    """
    return text.upper()

def reverse(text):
    """
    Megfordítja a kapott szöveget.

    Paraméterek:
        text(string): Bemeneti szöveg.
    
    Visszatér:
        A szöveg megfordított változata
    """
    return text[::-1]

def first_char(text):#meg kell nézni, nem üres-e a szöveg
    """
    Visszaadja a kapott szöveg első karakterét.

    Paraméterek:
        text(string): Bemeneti szöveg.
    
    Visszatér:
        Az első karakter, vagy 'None', ha a szöveg üres
    """
    if text=="":
        return None
    return text[0]