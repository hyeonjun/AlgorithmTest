n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
left, right = min(arr), sum(arr)
maxV = max(arr)
while left < right:
    mid = (left + right) // 2
    cnt, money = 1, mid # 인출 횟수
    for i in arr:
        if money < i:
            money = mid
            cnt += 1
        money -= i
    if cnt > m or mid < maxV:
        left = mid + 1
    else:
        right = mid
print(right)
