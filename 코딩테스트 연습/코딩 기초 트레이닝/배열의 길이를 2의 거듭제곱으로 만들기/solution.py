from math import ceil

def solution(arr):
    r, length = 0, len(arr)
    
    while length > 1:
        r += 1
        length = ceil(length / 2)
    
    answer = arr + [0] * (2 ** r - len(arr))
    return answer
