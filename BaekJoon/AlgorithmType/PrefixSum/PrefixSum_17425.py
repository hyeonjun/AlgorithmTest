import sys
input=sys.stdin.readline

prefix = [0 for _ in range(1000001)]

# 각 수의 배수는 전부 약수로 그 수를 포함 있음
for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        prefix[j] += i
    prefix[i] += prefix[i-1]

for _ in range(int(input())):
    print(prefix[int(input())])

# DP + PrefixSum
dp = [1 for _ in range(1000001)]
prefix = [0 for _ in range(1000001)]

for i in range(2, 1000001):
    j = 1
    while i * j <= 1000000:
        dp[i*j] += i
        j += 1

for i in range(1, 1000001):
    prefix[i] = prefix[i-1] + dp[i]

for _ in range(int(input())):
    print(prefix[int(input())])