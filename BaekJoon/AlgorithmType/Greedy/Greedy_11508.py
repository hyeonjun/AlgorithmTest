n = int(input())
price = [int(input()) for _ in range(n)]
price.sort(reverse=True)
answer = 0
for i in range(1, n+1):
    if i % 3 != 0:
        answer += price[i-1]
print(answer)