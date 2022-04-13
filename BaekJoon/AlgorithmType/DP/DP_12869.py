from itertools import permutations
n = int(input())
scv = list(map(int, input().split())) + [0 for _ in range(3-n)]
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]

def dfs(a, b, c):
    if a < 0: return dfs(0, b, c)
    if b < 0: return dfs(a, 0, c)
    if c < 0: return dfs(a, b, 0)
    if sum([a, b, c]) == 0: return 0
    if dp[a][b][c] != -1: return dp[a][b][c]

    dp[a][b][c] = 123456789
    for x, y, z in permutations([1, 3, 9]):
        dp[a][b][c] = min(dp[a][b][c], dfs(a-x, b-y, c-z)+1)
    return dp[a][b][c]

print(dfs(*scv))