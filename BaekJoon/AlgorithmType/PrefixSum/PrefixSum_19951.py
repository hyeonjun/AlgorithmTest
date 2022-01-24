n, m = map(int, input().split())
arr = list(map(int, input().split()))

delta = [0 for _ in range(n+1)]

for _ in range(m):
    a,b,k = map(int, input().split())
    delta[a-1] += k # 변화량 계산
    delta[b] -= k

# 누적합 계산
for i in range(1, n+1):
    delta[i] += delta[i-1]

for i in range(n):
    print(arr[i]+delta[i], end=' ')