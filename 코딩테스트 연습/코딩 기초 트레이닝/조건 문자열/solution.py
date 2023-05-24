def solution(ineq, eq, n, m):
    oprt = {">=": ">=", "<=": "<=", ">!": ">", "<!": "<"}
    answer = int(eval(str(n) + oprt[ineq + eq] + str(m)))
    return answer
