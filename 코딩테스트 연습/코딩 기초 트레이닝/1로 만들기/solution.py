from math import log

def solution(num_list):
    answer = sum([int(log(i, 2)) for i in num_list])
    return answer
