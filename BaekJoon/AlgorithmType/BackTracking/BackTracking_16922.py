import sys
sys.setrecursionlimit(10**9)
n = int(input())
roma = [1, 5, 10, 50]
result = [0 for _ in range(50*20+1)]
num = []
def dfs(start):
    if len(num) == n:
        print(*num)
        result[sum(num)] = 1
        return
    for i in range(start, len(roma)):
        num.append(roma[i])
        dfs(i)
        num.pop()
dfs(0)
print(sum(result))