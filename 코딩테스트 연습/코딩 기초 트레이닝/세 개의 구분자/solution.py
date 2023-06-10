def solution(myStr):
    answer = [""]
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if answer[-1] != "":
                answer.append("")
        else:
            answer[-1] += i
    
    if answer[-1] == "":
        answer.pop(-1)
    return answer if answer else ["EMPTY"]
