s, c = map(int, input().split())
arr = []
sumV = 0
left, right = 1, 0
for _ in range(s):
    x = int(input())
    right = max(right, x)
    sumV += x
    arr.append(x)
while left <= right:
    mid = (left+right) // 2
    cnt = 0
    for a in arr:
        cnt += a // mid
    if cnt >= c:
        left = mid+1
    else:
        right = mid-1
print(sumV - c * right)