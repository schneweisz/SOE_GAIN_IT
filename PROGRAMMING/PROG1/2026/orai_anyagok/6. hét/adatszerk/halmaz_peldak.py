"""
set - EGYEDI elemek, gyors tagságvizsgálat
"""

from adatok import LATOGATOK_LISTA

def egyedi_latogatok(latogatok):
    return set(latogatok)

def uj_latogato_e(ip,eddigiek):
    return ip not in eddigiek

def main():
    eddigiek=egyedi_latogatok(LATOGATOK_LISTA)
    
    print(f"Összes látogatás: {len(LATOGATOK_LISTA)}")
    print(f"Egyedi látogatók: {len(eddigiek)}")
    
    teszt_ip="10.0.0.5"
    
    print(f"{teszt_ip} új látogató? {uj_latogato_e(teszt_ip, eddigiek)}")
      
if __name__ == "__main__":
    main()