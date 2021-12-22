# permutations 활용
from itertools import permutations

n = int(input())
num = [i for i in range(1, n + 1)]
for i in permutations(num, n):
    print(*i)

# BackTracking
n = int(input())
num = []

def dfs():
    if len(num) == n:
        print(*num)
        return
    for i in range(1, n+1):
        if i not in num:
            num.append(i)
            dfs()
            num.pop()
dfs()