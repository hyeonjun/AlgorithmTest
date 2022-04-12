"""
추를 사용하는 경우의 수는 3가지
1. 추를 올린다
2. 추를 뺀다
3. 추를 사용하지 않는다
백트래킹 -> BackTracking/BackTracking_2629.py
"""
N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
sumV = sum(n)
dp = [False for _ in range(40001)] # 확인하고자 하는 구슬의 무게는 최대 40000이다.
dp[0] = True

for i in n:
    tmp = dp[:]
    for j in range(40001):
        if dp[j]:
            for k in [0, -1, 1]:
                v = abs(j+(i*k))
                tmp[v] = True
    dp = tmp[:]
for x in m:
    print("Y" if dp[x] else "N", end=" ")
