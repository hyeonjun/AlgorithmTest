"""
배낭 문제 - 모든 무게에 대하여 최대 가지를 저장하기
DP[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 최대 가치
각 물품의 번호 i에 따라서 최대 가치 테이블 DP[i][j]를 갱신

arr = [[물건 무게, 물건 가치] ... ]

DP[i][j] =
  if j < arr[i-1][0]:
    DP[i-1][j], 지금 넣을 물건의 무게가 현재 넣을 수 있는 무게보다 크면 이전 물건을 넣을 가치를 넣음
  if j >= arr[i-1][0]:    이전에 넣은 물건의 가치 VS 지금 넣을 물건의 무게를 빼고 남은 무게에 넣을 수 있는 최대 가치 + 지금 넣을 물건의 가치
    max(DP[i-1][j], DP[i-1][j-arr[i-1][0]] + arr[i-1][0])
"""

n, k = map(int, input().split()) # 물품 수, 버틸 수 있는 무게
arr = [list(map(int, input().split())) for _ in range(n)] # 각 물건 무게, 해당 물건 가치
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < arr[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1][0]] + arr[i-1][1])

print(dp[n][k])