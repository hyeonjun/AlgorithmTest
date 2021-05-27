# 탐욕 알고리즘(Greedy Algorithm)
# 최적의 해에 가까운 값을 구하기 위해 사용
# 여러 경우 중 하나를 결정해야할 때마다, 매 순간 최적이라고 생각되는 경우는 선택

# 문제 1 동전문제
"""
지불해야할 값이 4720원 일때 10원 50원 100원 500원으로 동전의 수가 가장 적게 지불하시오.
"""
def solution(payment, money):
    tmp = [0] * 4
    for i in range(4):
        tmp[i], payment = divmod(payment, money[i])
    return sum(tmp)

print(solution(4720, [500, 100, 50, 1]))

coin_list = [500, 100, 50, 1]
def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value//coin
        total_coin_count += coin_num
        value-=coin_num * coin
        details.append([coin,coin_num])
    return total_coin_count, details

print(min_coin_count(4720, coin_list))

# 문제 2 부분 배낭 문제
"""
무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
각 물건은 무게(w)와 가치(v)로 표현될 수 있음
물건을 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음(Fractional Knapsack Problem)
"""
def solution(data_list, limit):
    data_list.sort(key=lambda x:x[1]/x[0], reverse=True)
    weight, value = 0, 0
    data = []
    for i in data_list:
        last = 1 if weight + i[0] <= limit else (limit - weight) / i[0]
        weight += i[0] * last
        value += i[1] * last
        data.append([i[0], i[1], last])
    return weight, value, data
#            무게 가치
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
print(solution(data_list, 30))
