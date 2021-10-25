string = input()
n = len(string)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
result = [float('inf') for _ in range(n+1)]
result[0] = 0

# 길이 1
for i in range(1, n+1):
    dp[i][i] = 1

for i in range(1, n):
    if string[i-1] == string[i]:
        dp[i][i+1] = 1

# 길이 3
# i - 크기, j - 시작점. j에서 i만큼의 길이를 가진 문자열이 팰린드롬인지 확인
# 양 끝이 같고 안쪽 문자열이 팰린드롬이면 팰린드롬이다.
for i in range(2, n):
    for j in range(1, n-i+1):
        if string[j-1] == string[i+j-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1, n+1):
    result[i] = min(result[i], result[i-1] +1)
    for j in range(i+1, n+1):
        if dp[i][j] != 0: # 팰린드롬이면
            result[j] = min(result[j], result[i-1]+1)

print(result[n])
