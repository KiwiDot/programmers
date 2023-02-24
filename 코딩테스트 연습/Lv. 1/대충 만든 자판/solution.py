def solution(keymap, targets):
    keypad = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] in keypad:
                keypad[i[j]] = min(keypad[i[j]], j+1)
            else:
                keypad[i[j]] = j+1
                
    answer = []
    for i in targets:
        cnt = 0
        for j in i:
            if j not in keypad:
                answer.append(-1)
                break
            cnt += keypad[j]
        else:
            answer.append(cnt)
        
    return answer
