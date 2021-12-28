"""
dp[순서][열려있는방1][열려있는방2]
"""

n = int(input())
open1, open2 = map(int, input().split())
k = int(input())
order = [int(input()) for _ in range(k)]
dp = [[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(k+1)]

def move(idx, x, y):
    if idx == k:
        return 0
    if dp[idx][x][y] != -1:
        return dp[idx][x][y]

    dp[idx][x][y] = min(
        abs(order[idx]-x) + move(idx+1, order[idx], y),
        abs(order[idx]-y) + move(idx+1, x, order[idx])
    )
    return dp[idx][x][y]

print(move(0, open1, open2))