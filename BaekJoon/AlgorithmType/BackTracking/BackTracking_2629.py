"""
추를 사용하는 경우의 수는 3가지
1. 추를 올린다
2. 추를 뺀다
3. 추를 사용하지 않는다
다이나믹 프로그래밍 -> DP/DP_2629.py
"""
N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
visited = [[0 for _ in range((30 * 500) + 1)] for _ in range(N+1)]
candidate = set()
def dfs(idx, value):
    if value not in candidate:
        candidate.add(value)
    if idx == N:
        return

    if visited[idx][value] == 0:
        for i in range(idx, N):
            for j in [0, 1, -1]:
                visited[i][value] = 1
                dfs(i+1, abs(value+(n[i] * j)))
dfs(0, 0)
for x in m:
    print("Y" if x in candidate else "N", end=" ")