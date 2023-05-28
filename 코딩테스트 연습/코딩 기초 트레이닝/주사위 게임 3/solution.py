from collections import Counter

def solution(a, b, c, d):
    a, b, c, d = sorted([a, b, c, d])
    cnt = dict(Counter([a, b, c, d]))
    dice = dict()
    
    if len(cnt) == 1:
        answer = a * 1111
        
    elif len(cnt) == 2:
        if set(cnt.values()) == {2}:
            answer = (a + d) * abs(a - d)
        else:
            answer = 0
            for i in cnt:
                if cnt[i] == 1:
                    answer += i
                else:
                    answer += i * 10
            answer **= 2
        
    elif len(cnt) == 3:
        answer = 1
        for i in cnt:
            if cnt[i] == 1:
                answer *= i
        
    else:
        answer = a
        
    return answer
