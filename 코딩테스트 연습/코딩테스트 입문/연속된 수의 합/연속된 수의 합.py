# 난이도 Lv.0 - 연속된 수의 합
def solution(num, total):
    total -= num * (num - 1) // 2
    n = total // num
    answer = [n + i for i in range(num)]

    return answer