def solution(num_list):
    odd = ''.join([str(i) for i in num_list if i % 2])
    even = ''.join([str(i) for i in num_list if not i % 2])
    answer = int(odd) + int(even)
    return answer
