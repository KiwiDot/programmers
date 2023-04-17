def solution(players, callings):
    p = dict([(players[i], i) for i in range(len(players))])
    
    for name in callings:
        idx = p[name] - 1
        name2 = players[idx]
        
        players[idx], players[idx+1] = name, name2
        p[name] = idx
        p[name2] = idx + 1
        
    answer = players
    return answer
