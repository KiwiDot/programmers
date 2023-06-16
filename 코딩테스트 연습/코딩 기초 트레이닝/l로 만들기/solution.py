def solution(myString):
    answer = ''.join([i if i > 'l' else 'l' for i in myString])
    return answer
