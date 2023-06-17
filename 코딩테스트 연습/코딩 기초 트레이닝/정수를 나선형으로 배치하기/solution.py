def solution(n):
    answer = [[0] * n for i in range(n)]
    x, y = [-1], [0]
    d = {'R': [x, +1, n, 'D'],
         'D': [y, +1, n - 1, 'L'],
         'L': [x, -1, n - 1, 'U'],
         'U': [y, -1, n - 2, 'R']}
    drt = 'R'
    num = 1

    while num <= n ** 2:
        r = d[drt][2]

        for i in range(r):
            d[drt][0][0] += d[drt][1]
            xi, yi = x[0], y[0]
            answer[yi][xi] = num
            num += 1

        d[drt][2] -= 2
        drt = d[drt][3]

    return answer
