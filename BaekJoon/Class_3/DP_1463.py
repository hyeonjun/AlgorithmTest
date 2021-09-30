x = int(input())
dp = [0 for i in range(x+1)] # 각 원소 값은 횟수임
# 3으로 나누기, 2로 나누기, 1빼기
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # i는 i-1(1뻬기)의 연산 전으로 돌리면 나온다
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # i라는 수를 만들 때 1 빼기전과 랑 3으로 나누기 전 횟수 중 적은 것
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # 1뺀거랑 2로 나눈 것
print(dp[x])