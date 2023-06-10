def solution(arr, k):
    answer = []
    check = set()
    
    for i in arr:
        if i not in check:
            answer.append(i)
            check.add(i)
            
            if len(answer) == k:
                break
    else:
        answer += [-1] * (k - len(answer))
                
    return answer
