sum_of_positives=0
even_count=0
ok_count=0

while True:
    s=input("Szám :").strip()
    try:
        num=int(s)
    except ValueError:
        print("hiba: nem egész szám.")
        continue
    if num==0:
        break
    ok_count+=1
    if num>0:
        sum_of_positives+=num
    if num%2==0:
        even_count+=1