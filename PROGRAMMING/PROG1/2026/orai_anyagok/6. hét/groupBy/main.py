import itertools

"""
az itertoolsban beépített groupby függvény egy iterátor, amelyik csak egyszer megy végig
az adatokon

fontos: csak az egymás melletti (szomszédos), de azonos kulcsú elemeket csoportosít

"""


def t1_runs_of_equal_numbers(nums):
    """azonos számokat 1 csoportba"""
    out=[]
    for key, group_iter in itertools.groupby(nums):
        out.append((key,list(group_iter)))
    return out
    
def t2_runs_by_parity(nums):
    """páros-páratlan csoportok"""
    out=[]
    for key,group_iter in itertools.groupby(nums, lambda x: "even" if x%2==0 else "odd"):
        out.append((key,list(group_iter)))
    return out
def t3_group_words_by_first_letter(words):
    """szavak csoportosítása első betű szerint"""
    words_sorted=sorted(words, key=lambda x: x[0])
    out=[]
    for key,group_iter in itertools.groupby(words_sorted,key=lambda x: x[0]):
        out.append((key,list(group_iter)))
    return out

def t4_count_per_first_letter(words):
    """szavak száma első betű alapján"""
    words_sorted=sorted(words, key=lambda x: x[0])
    out=[]
    for key,group_iter in itertools.groupby(words_sorted,key=lambda x: x[0]):
        out.append((key, sum(1 for _ in group_iter))) #sum
    return out

def t7_group_students_by_major(students):
    """hallgatók csoportosítása szak szerint"""
    
    students_sorted=sorted(students,key=lambda x:x["major"])
    out=[]
    for major,group_iter in itertools.groupby(students_sorted, key=lambda x:x["major"]):
        out.append((major,list(group_iter)))
    return out

def t7_1_group_students_by_major(students):
    """hallgatók csoportosítása szak szerint CSAK NÉV"""
    
    students_sorted=sorted(students,key=lambda x:x["major"])
    out=[]
    for major,group_iter in itertools.groupby(students_sorted, key=lambda x:x["major"]):
        group_list=list(group_iter)
        out.append((major,[student["name"] for student in group_list]))
    return out

def t8_avarage_points_per_major(students):
    """átlag pontszám szak szerint"""
    students_sorted = sorted(students, key=lambda s: s["major"])
    out = []
    for major, group_iter in itertools.groupby(students_sorted, key=lambda s: s["major"]):
        group_list = list(group_iter)
        avg=sum(students["points"] for students in group_list)/len(group_list)
        out.append((major,avg))
    return out
def t9_group_students_by_year_and_major(students):
    """hallgatók csoportosítása év, majd szak szerint"""
    students_sorted=sorted(students,key=lambda x:(x["year"],x["major"]))
    out=[]
    for year,year_group_iter in itertools.groupby(students_sorted,key=lambda x:x["year"]):
        year_list=list(year_group_iter)
        majors=[]
        for major, major_group_iter in itertools.groupby(year_list,key=lambda x:x["major"]):
            majors.append((major,[s["name"] for s in major_group_iter]))
        out.append((year,majors))
    return out
    
    
    

def main():
    nums=[1,1,2,2,2,1,1,3,3,2]
    print("Feladat 1:", t1_runs_of_equal_numbers(nums))
    #Feladat 1: [(1, [1, 1]), (2, [2, 2, 2]), (1, [1, 1]), (3, [3, 3]), (2, [2])]
    print("Feladat 2:", t2_runs_by_parity(nums))
    #Feladat 2: [('odd', [1, 1]), ('even', [2, 2, 2]), ('odd', [1, 1, 3, 3]), ('even', [2])]
    print("main")
    words=["alma","ananász","banán","barack","cseresznye","alma","banán"]
    print("Feladat 3:", t3_group_words_by_first_letter(words))
    #[('a', ['alma', 'ananász', 'alma']), ('b', ['banán', 'barack', 'banán']), ('c', ['cseresznye'])] 
    print("Feladat 4:", t4_count_per_first_letter(words))
    #Feladat 4: [('a', 3), ('b', 3), ('c', 1)]
    STUDENTS=[
        {"name":"Anna","major":"prog","year":1,"points":80},
        {"name":"Béla","major":"prog","year":1,"points":55},
        {"name":"Csilla","major":"math","year":1,"points":92},
        {"name":"Dénes","major":"math","year":2,"points":66},
        {"name":"Eszter","major":"prog","year":2,"points":71},
        {"name":"Ferenc","major":"phys","year":1,"points":60},
        {"name":"Gabi","major":"phys","year":2,"points":88}
    ]
    print("Feladat 7:",t7_group_students_by_major(STUDENTS))
    print("Feladat 7_1:",t7_1_group_students_by_major(STUDENTS))
    #Feladat 7_1: [('math', ['Csilla', 'Dénes']), ('phys', ['Ferenc', 'Gabi']), ('prog', ['Anna', 'Béla', 'Eszter'])] 
    print("Feladat 8:",t8_avarage_points_per_major(STUDENTS))
    #Feladat 8: [('math', 79.0), ('phys', 74.0), ('prog', 68.66666666666667)]
    print("Feladat 9:",t9_group_students_by_year_and_major(STUDENTS))
    #Feladat 9: [(1, 
    #[('math', ['Csilla']), ('phys', ['Ferenc']), ('prog', ['Anna', 'Béla'])]), 
    #(2, [('math', ['Dénes']), ('phys', ['Gabi']), ('prog', ['Eszter'])])]
if __name__ == "__main__":
    main()