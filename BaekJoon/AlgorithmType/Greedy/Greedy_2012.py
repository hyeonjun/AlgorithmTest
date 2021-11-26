n = int(input())
rank = sorted([int(input()) for _ in range(n)])
answer = 0
for i in range(1, n+1):
    answer += abs(rank[i-1]-i)
print(answer)