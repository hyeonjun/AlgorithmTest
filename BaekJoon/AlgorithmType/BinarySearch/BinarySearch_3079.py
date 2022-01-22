n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
left, right = 0, max(arr) * m
while left < right:
    mid = (left+right) // 2 # 기준점 : 심사를 마치는 데 걸리는 최소 시간
    cnt = 0 # 해당 시간으로 심사를 할 수 있는 사람 수
    for a in arr:
        cnt += mid // a
    if cnt < m:
        left = mid+1
    else:
        right = mid
print(right)