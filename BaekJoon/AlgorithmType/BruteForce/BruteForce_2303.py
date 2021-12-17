from itertools import combinations
n = int(input())
card = [list(map(int, input().split())) for _ in range(n)]
answer = [0 for _ in range(n)]
for i in range(n):
    tmp = 0
    for c in combinations(card[i], 3):
        tmp = max(tmp, sum(c) % 10)
    answer[i] = tmp

maxV = max(answer)
for i in range(n-1, -1, -1):
    if answer[i] == maxV:
        print(i+1)
        break