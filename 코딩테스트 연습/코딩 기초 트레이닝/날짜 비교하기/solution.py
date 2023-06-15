def solution(date1, date2):
    date = sorted([date1, date2], key=lambda x: [x[0], x[1], x[2]])
    answer = int(date1 == date[0] and date[0] != date[1])
    return answer
