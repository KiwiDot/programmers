def solution(code):
    mode = 0
    ret = ''
    
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                ret += code[i]
                
    return ret if ret else "EMPTY"
