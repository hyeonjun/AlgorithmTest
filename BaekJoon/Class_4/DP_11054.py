n = int(input())
num = list(map(int, input().split()))
reverse_num = num[::-1]
dp_d = [1 for _ in range(n)]
dp_i = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if num[j] < num[i]:
            dp_i[i] = max(dp_i[i], dp_i[j]+1)
        if reverse_num[i] > reverse_num[j]:
            dp_d[i] = max(dp_d[i], dp_d[j]+1)

dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = dp_i[i] + dp_d[n-i-1] - 1

print(max(dp))