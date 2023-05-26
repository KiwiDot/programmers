def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        num = {arr[i] for i in range(s, e + 1) if arr[i] > k}
        answer.append(min(num) if num else -1)
    return answer
