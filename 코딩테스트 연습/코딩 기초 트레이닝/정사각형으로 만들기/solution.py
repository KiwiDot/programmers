def solution(arr):
    r, c = len(arr), len(arr[0])
    if r > c:
        answer = [i + [0] * (r - c) for i in arr]
    elif r < c:
        answer = arr + [[0] * c for i in range(c - r)]
    else:
        answer = arr
    return answer
