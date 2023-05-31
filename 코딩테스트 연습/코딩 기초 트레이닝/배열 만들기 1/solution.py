def solution(n, k):
    answer = [i for i in range(1, n+1) if not i % k]
    return answer
