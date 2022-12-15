# 난이도 Lv. 0 - 다음에 올 숫자
def solution(common):
    # 등차수열
    if common[0] + common[2] == common[1] * 2:
        d = common[1] - common[0]
        answer = common[-1] + d

    # 등비수열
    else:
        r = common[1] / common[0]
        answer = common[-1] * r

    return answer