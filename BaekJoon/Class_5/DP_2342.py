import sys
sys.setrecursionlimit(10**6)
arr = list(map(int, input().split()))
dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(len(arr))]

"""
왼발 0, 오른발 0, arr[0]을 밝아야할 때
min(solution(1, arr[0], 0) + 왼쪽발로 arr[0]밟기, solution(1, 0, arr[0]) + 오른쪽발로 arr[0]밟기) 
"""
def power(a, b):
    if a == b: # 같은 위치면 힘 1
        return 1
    elif a == 0: # 중앙이면 2
        return 2
    elif abs(b-a) == 2: # 반대편
        return 4
    else: # 다른 지점에서 인접 지점
        return 3


def solution(n, l, r):
    if n >= len(arr)-1: # 끝까지 왔으면
        return 0

    if dp[n][l][r] != -1: # 이미 지나갔으면
        return dp[n][l][r]

    dp[n][l][r] = min(solution(n+1, arr[n], r) + power(l, arr[n]), solution(n+1, l, arr[n]) + power(r, arr[n]))

    return dp[n][l][r]

print(solution(0,0,0))