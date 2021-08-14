def solution(price, money, count):
    return abs(min(0, money-price*(count+1)*count//2))
    # return abs(min(money - sum([price*i for i in range(1, count+1)]), 0))

print(solution(3, 20, 4)) # 10