#01 - Felhasználó Kezelés

## Probléma az eredeti kódban:

A `register_user()` függvény **túl sok dolgot csinál**:

### Felelősségek:
1. Bemeneti adatokat kér be
2. Validáció 
3. Adatbázis ellenőrzés (létezik-e)
4. Üzleti logika (kategória, kedvezmény meghatározása)
5. Adatmentés (globális változóba)
6. Email "küldése" (print)
7. Statisztika számítás
8. Fájlba mentés
9. Eredmény kiírás

### További problémák:
- Globális állapot kezelés
- Nem tesztelhető
- Nem újrafelhasználható
- Nehéz karbantartani
- 100+ sor egy függvény (=>túl sok dolgokért felelős)

## Javasolt megoldás:
### Tiszta függvények csoportosítása:

#### 1. Validációs függvények:
- `is_valid_email()` - email formátum ellenőrzés
- `is_valid_password()` - jelszó követelmények
- `is_valid_age()` - életkor tartormány
- `is_valid_name()` - név hossz

#### 2. Üzleti logika:
- `determine_user_category()` - kategória meghatározása
- `calculate_discount()` - kedvezmény számítás
- `create_user()` - user objektum létrehozás
- `email_exists()` - duplikáció ellenőrzés
- `create_welcome_email()` - email szövég generálás
- `calculate_statistics()` -  statisztika számítása

#### 3. Input kezelés:
- `read_email()` - email bekérése
- `read_password()` - jelszó bekérése
- `read_name()` - név bekérése
- `read_age()` - kor bekérése

#### 4. Output kezelés:
- `print_welcome_message()`- üzenet kiírás
- `print_statistics` - statisztika kiírás
- `save_users_to_file` - fájlba mentés

#### 5. Koordináció:
- `register_user()` - összehangolja a folyamatot

## Előnyök

 **Tesztelhető**: Minden tiszta függvény külön tesztelhető 
 **Újrafelhasználható**: Függvények más kontextusban is használhatók 
 **Karbantartható**: Kis, érthető függvények 
 **Bővíthető**: Új validáció vagy logika könnyen hozzáadható 
 **Olvasható**: Egyértelmű függvénynevek és felelősségek 