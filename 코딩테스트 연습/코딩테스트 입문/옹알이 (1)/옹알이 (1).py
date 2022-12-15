# 난이도 Lv. 0 - 옹알이 (1)
def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        for j in word:
            i = i.replace(j, '-')

        if set(i) == {'-'}:
            answer += 1

    return answer
