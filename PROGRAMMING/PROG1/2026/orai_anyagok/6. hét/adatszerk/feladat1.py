"""
Adott egy beléptető rendszer és erőforrás-napló (log)

logbejegyzés szerkezet: (időpont,felhasználó,művelet,erőforrás)

FELADATOK:
1) Írd ki, mely felhasználók jelentek meg először,az első megjelenésük sorrendjében
2) Számold meg, hogy felhasználónként hány művelet történt
3) Add meg az összes EGYEDI erőforrást, amihez bárki hozzányúlt
4) Készíts egy olyan lekérdezést, amivel az adott felhasználó utolsó műveletét gyorsan megtudod mondani.
"""

LOG = [
    ("08:00", "anna", "login", "wifi"),
    ("08:01", "bela", "login", "wifi"),
    ("08:03", "anna", "open", "moodle"),
    ("08:04", "csilla", "login", "wifi"),
    ("08:05", "anna", "download", "python_ppt"),
    ("08:06", "bela", "open", "moodle"),
    ("08:07", "dori", "login", "wifi"),
    ("08:08", "bela", "submit", "hf1"),
    ("08:09", "csilla", "open", "teams"),
    ("08:10", "anna", "logout", "wifi"),
    ("08:11", "csilla", "download", "hf1"),
]
#https://pastebin.com/2jcYA0dq

#lista, tuple, dict, set
# a LOG "nyers" formában van, egy listában vannak a bejegyzések, mivel fontos a sorrend!
#1) set 
#2) dict
#3) set 
#4) dict

def elso_megjelenesi_sorrend(log):
    latott=set()
    sorrend=[]
    #("08:00", "anna", "login", "wifi"),
    for _,user,_,_ in log:
        if user not in latott:
            latott.add(user)
            sorrend.append(user)
    
    return sorrend

def muveletek_szama_felhasznalonkent(log):
    db={}
    
    for _,user,_,_ in log:
        db[user]=db.get(user,0)+1
    
    return db
    
def egyedi_eroforrasok(log):
    eroforrasok=set()
    
    for _,_,_,res in log:
        eroforrasok.add(res)
        
    return eroforrasok

def utolso_muvelet_gyorsan(log):
    utolso={}
    
    for t,user,action,res in log:
        utolso[user]=(t,action,res)
    return utolso    

def main():
    print("1) Első megjelenési sorrend:")
    print(elso_megjelenesi_sorrend(LOG))
    #['anna', 'bela', 'csilla', 'dori']
    
    print("\n2) Műveletek száma felhasználónként:")
    counts = muveletek_szama_felhasznalonkent(LOG)
    for user in sorted(counts):
        print(f"- {user}: {counts[user]}")
    """
    - anna: 4
    - bela: 3
    - csilla: 3
    - dori: 1
    """
    
    print("\n3) Egyedi erőforrások:")
    print(egyedi_eroforrasok(LOG))
    #{'wifi', 'moodle', 'python_ppt', 'hf1', 'teams'}
    print("\n4) Utolsó művelet gyorsan:")
    last=utolso_muvelet_gyorsan(LOG)
    for user in sorted(last):
        t,action,res=last[user]
        print(f"- {user}: {t} - {action} - {res}")
        
    #a feladat keresés része:
    keresett="bela"
    t,action,res=last[keresett]
    print(f"\n{keresett} utolsó művelete: {t} - {action} - {res}")
    #bela utolsó művelete: 08:08 - submit - hf1
if __name__ == "__main__":
    main()
