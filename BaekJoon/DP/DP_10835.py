"""
dp[i][j] => i : 왼쪽, j : 오른쪽

왼쪽보다 오른쪽이 작을 때,
 1. 둘 다 버림
 2. 왼쪽만 버림
 3. 오른쪽 버리고 점수 얻음

오른쪽이 왼쪽보다 크거나 같을 때
 1. 둘 다 버림
 2. 왼쪽만 버림

"""
import sys
input = sys.stdin.readline

# bottom top 방식
n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if right[j] < left[i]:
            dp[i][j] = max(dp[i+1][j+1], dp[i][j+1]+right[j], dp[i+1][j])
        else:
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])
print(dp[0][0])