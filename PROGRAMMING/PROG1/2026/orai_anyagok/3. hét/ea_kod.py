def filter_positive(numbers):
    positives=[]
    for n in numbers:
        if n>0:
            positives.append(n)
    return positives

def average(numbers):
    if not numbers:
        return None
    total=0
    for n in numbers:
        total+=n
    return total/len(numbers)

def sum_and_count(numbers):
    total=0
    count=0
    for n in numbers:
        total+=n
        count+=1
    return total,count

def main():
    numbers=[1,3,-2,5,-1,4]
    positives=filter_positive(numbers)
    avg=average(positives)
    total,count=sum_and_count(positives)
    
    print(positives)
    print(avg)
    print(total)
    print(count)
    
if __name__=="__main__":
    main()