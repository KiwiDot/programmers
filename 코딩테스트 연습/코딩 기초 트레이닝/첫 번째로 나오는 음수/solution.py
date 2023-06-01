def solution(num_list):
    for answer in range(len(num_list)):
        if num_list[answer] < 0:
            return answer
    return -1
