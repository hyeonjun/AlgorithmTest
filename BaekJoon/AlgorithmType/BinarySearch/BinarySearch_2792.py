n, m = map(int, input().split())
arr = []
left, right = 1, 0
for _ in range(m):
    x = int(input())
    if right < x:
        right = x
    arr.append(x)

while left <= right:
    mid = (left+right) // 2 # 보석을 나눠줄 개수
    cnt = 0 # 나눠줄 수 있는 총 사람 수
    for a in arr:
        cnt += (a // mid) if not a % mid else (a // mid) + 1
    if cnt > n:
        left = mid+1 # left를 늘려서 나눠줄 수 있는 보석 개수를 크게 함
    else:
        right = mid-1
print(left)