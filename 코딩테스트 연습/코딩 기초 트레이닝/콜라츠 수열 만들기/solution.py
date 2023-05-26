def solution(n):
    answer = []
    
    while n != 1:
        answer.append(n)
        n = 3 * n + 1 if n % 2 else n // 2
    
    return answer + [1]
