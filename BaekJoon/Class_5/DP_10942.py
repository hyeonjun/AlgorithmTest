"""
팰린드롬
단어 길이 1 -> O
단어 길이 2 -> 같은 문자면 O, 다른 문자면 X
단어 길이 3 이상 ->
 1) 양 끝의 두 문자가 같음
 2) 1)을 만족하면서 양 끝의 두 문자를 제외하고 안에 있는 단어가 팰린드롬이면 O
"""
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)] # dp[start][end]

for i in range(n): # 길이 1인 경우
    dp[i][i] = 1

for i in range(n-1): # 길이 2인 경우
    if num[i] == num[i+1]:
        dp[i][i+1] = 1

for i in range(2, n): # 길이 3인 경우
    for j in range(n-i):
        if num[j] == num[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

# 0 1 2 3 4
# 1 2 3 2 1
# i -> 2 3 4 5, j -> 3 2 1 0
# i+j =>
#   i=2, j=0, 1, 2, i+j=2, 3, 4 (길이 3)
#       -> 1 != 3 x
#       -> 2 == 2 and dp[2][2] == 1 O (양 끝이 같고 양 끝 사이 문자열이 팰린드롬이면 O)
#               -> dp[1][3] = 1
#       -> 3 != 1 x
#   i=3, j=0, 1, i+j=3, 4 (길이 4)
#       -> 1 != 2 x
#       -> 2 != 4 x
#   i=4, j=0, i+j=4 (길이 5)
#       -> 1 == 1 and dp[1][3] == 1
#               -> dp[0][4] = 1