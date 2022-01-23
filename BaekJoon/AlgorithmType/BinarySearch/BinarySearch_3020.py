# Binary Search
n, h = map(int, input().split())
up, down = [], []
for i in range(n): # 가로
    s = int(input())
    if i % 2: # 홀수
        up.append(s)
    else:
        down.append(s)
up.sort()
down.sort()
minV, count = n, 0

def binary(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2 # 깨지 않고 지나갈 수 있는 장애물 개수
        if arr[mid] < x: # 해당 장애물 높이가 날고 있는 높이보다 낮으면
            left = mid+1
        else:
            right = mid-1
    return left # 깨지 않고 지나갈 수 있는 최대 개수

for i in range(1, h+1):
    cnt = n - (binary(up, h+1-i) + binary(down, i)) # 깨야할 장애물 개수
    if cnt == minV:
        count += 1
    elif cnt < minV:
        count = 1
        minV = cnt
print(minV, count)