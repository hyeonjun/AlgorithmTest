from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
for i in range(1, n+1):
    for c in combinations(arr, i):
        a, b = 1, 0
        for x, y in c:
            a *= x
            b += y
        answer = min(answer, abs(a-b))
print(answer)
