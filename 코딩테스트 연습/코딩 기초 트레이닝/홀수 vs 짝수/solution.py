def solution(num_list):
    answer = [0, 0]
    for i in range(len(num_list)):
        answer[i % 2] += num_list[i]
    return max(answer)
