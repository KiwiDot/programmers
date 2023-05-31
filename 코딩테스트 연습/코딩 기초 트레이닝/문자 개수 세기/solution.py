from collections import Counter

def solution(my_string):
    cnt = dict(Counter(my_string))
    answer = [cnt[chr(i+65)] if chr(i+65) in cnt else 0 for i in range(26)] + [cnt[chr(i+97)] if chr(i+97) in cnt else 0 for i in range(26)]
    return answer
