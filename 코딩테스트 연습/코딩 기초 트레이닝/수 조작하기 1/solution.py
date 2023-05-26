def solution(n, control):
    c = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    answer = n + sum([c[i] for i in control])
    return answer
