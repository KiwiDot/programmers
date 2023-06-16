def solution(order):
    price = {"americano": 4500, "cafelatte": 5000, "anything": 4500}
    answer = 0
    
    for i in order:
        for j in price:
            if j in i:
                answer += price[j]
                break
    return answer
