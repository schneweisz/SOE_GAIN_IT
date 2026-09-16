def read_data_hardcoded():
	# I. módszer: kódba beégetett tömb (mm/nap)
	return [0, 12, 5, 0, 3, 10, 0, 8, 0, 1]


def _read_int(prompt):
	while True:
		raw = input(prompt).strip()
		try:
			return int(raw)
		except ValueError:
			print("Hibás szám. Próbáld újra.")


def read_data_user():
	# II. módszer: a felhasználótól kérünk be adatokat manuálisan
	n = _read_int("Hány nap adatait adod meg? ")
	while n <= 0:
		print("A napok száma legyen pozitív.")
		n = _read_int("Hány nap adatait adod meg? ")

	print(
		"Add meg a csapadékot mm-ben (nemnegatív egész), egymás után.\n"
		"Írhatod egy sorba szóközzel elválasztva, vagy több sorban is."
	)

	values = []
	while len(values) < n:
		remaining = n - len(values)
		line = input(f"Még {remaining} db szám kell: ").strip()
		if not line:
			continue

		parts = line.split()
		ok = True
		parsed = []
		for p in parts:
			try:
				v = int(p)
			except ValueError:
				ok = False
				break
			if v < 0:
				ok = False
				break
			parsed.append(v)

		if not ok:
			print("Hibás bemenet. Csak nemnegatív egész számokat adj meg.")
			continue

		values.extend(parsed)

	return values[:n]


def analyze_rain(rain_mm):
	if not rain_mm:
		raise ValueError("Nincs adat.")

	# 1) megszámlálás: esős napok száma (esős: > 0)
	rainy_days_count = 0
	for v in rain_mm:
		if v > 0:
			rainy_days_count += 1

	# 2) maximum keresés
	max_value = rain_mm[0]
	for v in rain_mm[1:]:
		if v > max_value:
			max_value = v

	# 3) maximum érték helye (első előfordulás)
	max_day = 1
	for i in range(1, len(rain_mm)):
		if rain_mm[i] > rain_mm[max_day - 1]:
			max_day = i + 1

	# 4) összegzés: összes és átlag
	total = 0
	for v in rain_mm:
		total += v
	avg = total / len(rain_mm)

	# 5) minimum keresés
	min_value = rain_mm[0]
	for v in rain_mm[1:]:
		if v < min_value:
			min_value = v

	# 6) minimum érték helye (első előfordulás)
	min_day = 1
	for i in range(1, len(rain_mm)):
		if rain_mm[i] < rain_mm[min_day - 1]:
			min_day = i + 1

	# 7) eldöntés: volt-e olyan nap, amikor legalább 10 mm eső esett?
	# (Ha nálatok "10 mm-nél több" kell, cseréld >= 10-et > 10-re.)
	any_ge_10 = False
	for v in rain_mm:
		if v >= 10:
			any_ge_10 = True
			break

	# 8) kiválogatás: száraz napok (0 mm)
	dry_days = []
	for i, v in enumerate(rain_mm, start=1):
		if v == 0:
			dry_days.append(i)

	# 9) szétválogatás: esős és száraz napok két halmazba
	rainy_days = []
	dry_days2 = []
	for i, v in enumerate(rain_mm, start=1):
		if v > 0:
			rainy_days.append(i)
		else:
			dry_days2.append(i)

	# 10) keresés: első esős nap
	first_rainy_day = None
	for i, v in enumerate(rain_mm, start=1):
		if v > 0:
			first_rainy_day = i
			break

	# 11) optimista eldöntés: igaz-e, hogy minden nap esett (minden > 0)?
	all_rainy = True
	for v in rain_mm:
		if v <= 0:
			all_rainy = False
			break

	return {
		"rainy_days_count": rainy_days_count,
		"max_value": max_value,
		"max_day": max_day,
		"total": total,
		"avg": avg,
		"min_value": min_value,
		"min_day": min_day,
		"any_ge_10": any_ge_10,
		"dry_days": dry_days,
		"rainy_days": rainy_days,
		"dry_days2": dry_days2,
		"first_rainy_day": first_rainy_day,
		"all_rainy": all_rainy,
	}


def print_data(rain_mm):
	print("\nBeolvasott adatok (nap: mm):")
	for i, v in enumerate(rain_mm, start=1):
		print(f"  {i}. nap: {v} mm")


def main():
	print("Csapadék adatelemzés")
	print("1) Beégetett tömb")
	print("2) Kézi adatbevitel")

	choice = input("Válassz (1/2): ").strip()
	while choice not in {"1", "2"}:
		choice = input("Válassz (1/2): ").strip()

	if choice == "1":
		rain_mm = read_data_hardcoded()
	else:
		rain_mm = read_data_user()

	print_data(rain_mm)
	result = analyze_rain(rain_mm)

	print("\nEredmények:")
	print(f"1) Esős napok száma: {result['rainy_days_count']}")
	print(f"2) Legtöbb eső (max): {result['max_value']} mm")
	print(f"3) A legtöbb eső napja (max helye): {result['max_day']}. nap")
	print(f"4) Összes eső: {result['total']} mm; átlag: {result['avg']:.2f} mm/nap")
	print(f"5) Legkevesebb eső (min): {result['min_value']} mm")
	print(f"6) A legkevesebb eső napja (min helye): {result['min_day']}. nap")
	print(f"7) Volt-e legalább 10 mm-es nap? {'igen' if result['any_ge_10'] else 'nem'}")
	dry_days = result["dry_days"]
	print(f"8) Száraz napok (0 mm): {dry_days if dry_days else 'nincs'}")
	print(f"9) Esős napok: {result['rainy_days']}; száraz napok: {result['dry_days2']}")
	first_rainy = result["first_rainy_day"]
	print(f"10) Első esős nap: {str(first_rainy) + '. nap' if first_rainy is not None else 'nincs'}")
	print(f"11) Igaz-e, hogy minden nap esett? {'igen' if result['all_rainy'] else 'nem'}")


if __name__ == "__main__":
	main()
