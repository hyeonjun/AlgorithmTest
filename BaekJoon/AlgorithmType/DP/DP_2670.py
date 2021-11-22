"""
     1       2       3          4       5  6  7  8
     1    1*2, 2  dp[i-1]*3 3
arr[i] = max(arr[i], arr[i]*arr[i-1)
"""
# round의 경우 1.00000일때 소수점 넷째자리에서 반올림하라고 해도 1.0으로 출력된다
n = int(input())
arr = [float(input()) for _ in range(n)]
for i in range(1, n):
    arr[i] = max(arr[i], arr[i]*arr[i-1])
print("%.3f" % max(arr))

