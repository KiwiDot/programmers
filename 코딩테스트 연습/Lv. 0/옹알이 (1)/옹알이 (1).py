# 프로그래머스 Lv. 0 옹알이 (1)
import sys
put = sys.stdin.readline

def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        for j in word:
            i = i.replace(j, '-')

        if set(i) == {'-'}:
            answer += 1

    return answer