from collections import Counter

def solution(strArr):
    group = dict(Counter([len(i) for i in strArr]))
    answer = max(group.values())
    return answer
