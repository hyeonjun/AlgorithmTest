n, m = map(int, input().split())
arr = list(map(int, input().split()))
left, right = max(arr), sum(arr)
while left <= right:
    mid = (left+right) // 2 # 기준점 : 블루레이 크기
    flag = True
    bluray = [0 for _ in range(m)]
    idx = 0
    for i in range(n):
        if bluray[idx] + arr[i] <= mid:
            bluray[idx] += arr[i]
        else:
            idx += 1
            if idx == m:
                flag = False
                break
            bluray[idx] += arr[i]
    if not flag:
        left = mid+1
    else:
        right = mid-1
print(left)