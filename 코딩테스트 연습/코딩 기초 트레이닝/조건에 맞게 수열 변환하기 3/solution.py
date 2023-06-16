def solution(arr, k):
    answer = [i * k for i in arr] if k % 2 else [i + k for i in arr]
    return answer
