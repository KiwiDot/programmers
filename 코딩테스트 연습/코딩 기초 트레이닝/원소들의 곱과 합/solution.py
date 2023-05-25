def solution(num_list):
    check1, check2 = 1, 0
    for i in num_list:
        check1 *= i
        check2 += i

    answer = 1 if check1 < check2 ** 2 else 0
    return answer
