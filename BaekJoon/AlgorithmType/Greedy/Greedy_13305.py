n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
p = price[0]
answer = 0
for i in range(n-1):
    if p > price[i]:
        p = price[i]
    answer += p * road[i]
print(answer)