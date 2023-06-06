def solution(arr):
    answer = 0
    arr2 = []
    
    while True:
        arr2 = [i // 2 if i >= 50 and not i % 2 else (i * 2 + 1 if i <= 50 and i % 2 else i) for i in arr]
        if arr == arr2:
            break
        arr = arr2.copy()
        answer += 1
    return answer
