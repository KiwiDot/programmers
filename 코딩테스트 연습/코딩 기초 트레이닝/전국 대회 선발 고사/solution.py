def solution(rank, attendance):
    ranking = sorted([[rank[i], i] for i in range(len(rank)) if attendance[i]])
    a, b, c = ranking[0][1], ranking[1][1], ranking[2][1]
    answer = 10000 * a + 100 * b + c
    return answer
