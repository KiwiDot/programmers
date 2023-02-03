def solution(s, skip, index):
    skip = set(skip)
    alphabet = ''
    for i in range(26):
        alphabet += chr(i + 97) if chr(i + 97) not in skip else ''
    a = len(alphabet)
    
    dct = dict([(alphabet[i], alphabet[(i+index)%a]) for i in range(a)])
    answer = ''.join([dct[i] for i in s])
    
    return answer
