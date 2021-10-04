import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix_sum = [0]
for i in num:
    prefix_sum.append(i+prefix_sum[-1])

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
"""
num = [5, 4, 3, 2, 1]
prefix_sum = [0, 5, 9, 12, 14, 15]
ex) 0~2 범위의 구간 합
-> num[0] + num[1] + num[2] = 5 + 4 + 3 = 12
-> prefix_sum[3] - prefix_sum[0] = 12 - 0 = 12
ex) 1~3 범위 구간 합
-> num[1] + num[2] + num[3] = 9
-> prefix_sum[4] - prefix_sum[1] = 14 - 5 = 9
"""