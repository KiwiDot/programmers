def solution(name, yearning, photo):
    score = dict([(name[i], yearning[i]) for i in range(len(name))])
    answer = []
    
    for i in photo:
        answer.append(sum([score[j] if j in score else 0 for j in i]))
    return answer
