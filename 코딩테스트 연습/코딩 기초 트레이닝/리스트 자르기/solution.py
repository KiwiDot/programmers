def solution(n, slicer, num_list):
    a, b, c = slicer
    answer = {1: num_list[:b+1], 2: num_list[a:], 3: num_list[a:b+1], 4: num_list[a:b+1:c]}
    return answer[n]
