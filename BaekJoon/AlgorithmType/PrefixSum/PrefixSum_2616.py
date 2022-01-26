n = int(input())
arr = list(map(int, input().split()))
m = int(input())

prefix = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i-1]

dp = [[0 for _ in range(n+1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(m, n+1):
        # i 번째 기관차의 이전 최대값 vs i-1번 째 기관차의 최대값 + 현재 기관차의 m 번째 승객 선택 시 승객 수
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + prefix[j]-prefix[j-m])

print(dp[3][n])