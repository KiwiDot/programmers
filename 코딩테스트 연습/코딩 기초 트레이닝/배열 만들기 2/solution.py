from itertools import product

def solution(l, r):
    answer = []
    for i in range(len(str(l)), len(str(r)) + 1):
        for j in product(['0', '5'], repeat=i-1):
            n = int('5' + ''.join(j))
            if l <= n <= r:
                answer.append(n)
    return answer if answer else [-1]
