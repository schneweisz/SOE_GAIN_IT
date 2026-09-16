"""
Implementáld az alábbi függvényeket!
"""

import doctest


def caesar_cipher(text, offset):
    """Előállítja a szöveg Caesar-rejtjelezett változatát a megadott eltolással.

    A szövegben minden betűt lecserél az ábécében megadott távolságban lévő betűre.
    Az angol ábécét használja, és nagybetűsre alakítja a szöveget.
    https://hu.wikipedia.org/wiki/Caesar-rejtjel
    >>> caesar_cipher('alma', 2)
    'CNOC'
    >>> caesar_cipher('A big xylophone!', 4)
    'E FMK BCPSTLSRI!'
    """
    text = text.upper()
    result = ""

    for char in text:
        if 'A' <= char <= 'Z':
            new_char = chr(((ord(char) -65 + offset) % 26 ) + 65)
        else:
            new_char = char
        result += new_char
    return result

def vigenere_cipher(text, password):
    """Előállítja a szöveg Vigenère-rejtjelezett változatát a kapott jelszóval.

    A szövegben minden betűre alkalmaz egy Caesar-kódolást, de a jelszó betűi határozzák
    meg az eltolás mértékét: A=1, B=2, stb.
    Az 1. betűre az eltolást a jelszó 1. betűje határozza meg, a 2. betűre a jelszó 2.
    betűje, stb. A jelszó utolsó betűje után ismét az 1. betűje, 2. betűje, stb.
    Az ábécében nem szereplő karaktereket változatlanul hagyja és nem veszi figyelembe
    az eltolás meghatározásakor.
    >>> vigenere_cipher('ABCDEF', 'ADG')
    'BFJEIM'
    >>> vigenere_cipher('EZ *TITOK*', 'AHA')
    'FH *UJBPL*'
    """
    text = text.upper()
    password = password.upper()
    password_idx = 0
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            shift = ord(password[password_idx]) - ord('A') + 1
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) 
            password_idx = (password_idx + 1) % len(password)
        else:
            new_char = char
        result += new_char    
    return result



def vigenere_decipher(encoded_text, password):
    """Dekódolja a Vigenère-rejtjelezett szöveget a megadott jelszóval.
    >>> vigenere_decipher('BFJEIM', 'ADG')
    'ABCDEF'
    >>> vigenere_decipher('FH *UJBPL*', 'AHA')
    'EZ *TITOK*'
    """
    encoded_text = encoded_text.upper()
    password = password.upper()
    password_idx = 0
    result = ""
    
    for char in encoded_text:
        if 'A' <= char <= 'Z':
            shift = ord(password[password_idx]) - ord('A') + 1
            new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            password_idx = (password_idx + 1) % len(password)
        else:
            new_char = char
        result += new_char
        
    return result


if __name__ == "__main__":
    doctest.testmod()
