# 🧠 PROGRAMOZÁS 1 - ZH TÚLÉLŐKÖNYV ÉS LOGIKAI VÁZLAT

## 1. Döntési fa: Hogyan induljak el, ha meglátok egy feladatot?

Ne kezdj el azonnal kódolni! Futtasd le ezt a 4 kérdést a fejedben:

1. **Milyen formában kapom az adatot?**
   - Ha egy nagy string: Fel kell vágni sorokra (`.strip().split("\n")`).
   - Van végjel (`VEGE`) vagy üres sor? Kell rá egy `if` feltétel.

2. **Mit akarok a végén visszakapni? (Milyen legyen a gyűjtődoboz?)**
   - Csak adatok listázása -> `Lista []`
   - Egyediséget kell vizsgálni / duplikátumot szűrni -> `Halmaz set()`
   - Valami (pl. név) ALAPJÁN kell keresni/számolni -> `Szótár {}`
   - Nevenként csoportosított EGYEDI adatok -> `Szótár halmazokkal (Dict-of-Sets)`
   - Nevenként csoportosított MINDEN tranzakció -> `Szótár listákkal (Dict-of-Lists)`

3. **Milyen "szemetet" kell azonnal kidobnom?**
   - Határozd meg a "hibás" sor feltételeit (rossz akció neve, negatív szám). Ezt azonnal, a feldolgozó `for` ciklusod legelején zárd ki egy `if feltétel: continue` paranccsal!

4. **Külön tudom választani a lépéseket?**
   - SOHA ne csinálj mindent egyetlen funkcióban!
   - FÜGGVÉNY 1: Csak beolvas, megtisztít, és visszaadja a kész, tiszta Szótárat.
   - FÜGGVÉNY 2: Megkapja a Szótárat, és kikeresi belőle az átlagot/statisztikát.

---

## 2. A 4 Leggyakoribb Programozási Minta

### A) A "Folyosó-ellenőr" (Adattisztítás)

- **Tipikus szöveg:** "hagyd figyelmen kívül", "ha az érték hibás", "csak érvényes akciók".
- **Stratégia:** Korai kilépés (`continue`). Ne csinálj hatalmas `if-else` fészket. Tedd fel a kérdést: "Mi tesz egy sort hibássá?". Ha hibás, azonnal `continue`.

### B) A "Postázó" (Csoportosítás szótárba)

- **Tipikus szöveg:** "felhasználónként gyűjtsd össze", "kategóriánként", "ki mit csinált".
- **Stratégia:** 1. Vizsgáld meg, van-e már ilyen kulcs a szótárban (`if nev not in szotar`). 2. Ha nincs, hozz létre egy üres listát/halmazt hozzá. 3. Fűzd hozzá/add hozzá az aktuális adatot.

### C) A "Könyvelő" (Összegzés és számlálás)

- **Tipikus szöveg:** "hányszor fordult elő", "összesen mennyit költött", "szógyakoriság".
- **Stratégia:** Inicializálj nulláról. Iterálj a tiszta adaton, és minden találatnál növeld az értéket (`+= 1` vagy `+= ar`). Figyelj a típuskonverzióra (`int()`)!

### D) A "Dobogó" (Rendezés és Top lista)

- **Tipikus szöveg:** "leggyakoribb", "legjobb", "top 2 vásárló", "csökkenő sorrendben".
- **Stratégia:** Előbb MINDIG aggregálj (számolj mindent össze egy szótárba). A `sorted()` függvénynek a szótár `.items()` részét add át. Többszempontos rendezésnél használj stabil (kétlépcsős) rendezést. A végén vágd le a listát (`[:5]`).

---

## 3. A Leggyakoribb ZH Hibák (Erre figyelj!)

- **Láthatatlan szóközök:** A sorok végén maradt `\n` vagy szóköz megöli az `if == "VEGE"` feltételeket. Mindig `strip()`-eld a sort mielőtt vizsgálnád!
- **Típuseltérés:** Ha a `"1200"` string marad, nem tudod összeadni! A darabolás (`split`) után mindig csinálj belőle `int()`-et.
- **Szótár véletlen felülírása:** A `szotar[kulcs] = ertek` letörli az előző adatot. Ha gyűjteni akarsz, mindig hozz létre először egy gyűjtőt, és utána `szotar[kulcs].append(ertek)`.
- **Azonos darabszám eltűnése:** Halmazokba (`set`) hiába teszel kétszer "almát", csak egy marad! Ha a gyakoriság (darabszám) is számít, használj listát vagy számláló szótárat.
- **Rossz helyen lévő `return`:** Ha a `return` parancsot behúzod a `for` cikluson belülre, a program az első sor beolvasása után azonnal kilép a függvényből! Mindig ellenőrizd a behúzást (indentation).
