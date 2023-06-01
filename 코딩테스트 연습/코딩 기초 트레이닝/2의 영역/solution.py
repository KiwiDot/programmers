def solution(arr):
    arr = ' '.join([str(i) for i in arr])
    a, b = arr.find('2'), arr.rfind('2')
    answer = [int(i) for i in arr[a:b+1].split()] if a >= 0 and b >= 0 else [-1]
    return answer
