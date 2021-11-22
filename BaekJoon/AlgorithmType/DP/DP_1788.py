"""
dp[i] =
    if i=0, 0
    if i=1, 1
    if i>1, dp[i-1]+dp[i-2]
양수
 1  2  3  4  5
 1  1  2  3  5
음수
-1 -2 -3 -4 -5
 1 -1  2 -3  5
=> index가 음수이면서 짝수일 경우에만 음수 값이 나온다
"""
n = int(input())
dp = [0, 1]
mod = 1000000000
for i in range(2, abs(n)+1):
    dp.append((dp[i-1]+dp[i-2]) % mod)
if n == 0:
    print(0)
elif n < 0 and n % 2 == 0:
    print(-1)
else:
    print(1)
print(dp[abs(n)])