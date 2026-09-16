from collections import defaultdict
#ha nincs érték, alapértelmezetten ad neki egyet

def sum_numbers(numbers: list[int])->int:
    total =0
    for item in numbers:
        total+=item
    return total

def group_scores_by_course(pairs: list[tuple[str,int]])-> dict[str,list[int]]:
    grouped=dict[str,list[int]]=defaultdict(list)
    for course_name,score in pairs:
        grouped[course_name].append(score)
    return dict(grouped)

def average_scores_by_course(pairs: list[tuple[str,int]])-> dict[str,float]:
    grouped_scores=group_scores_by_course(pairs)
    return {
        course_name:sum(scores)/len(scores)
        for course_name,scores in grouped_scores.items()
    }