# 절단기 높이 : 기준
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
while start <= end:
    mid = (start+end) // 2
    height = 0
    for t in tree:
        if t > mid:
            height += t-mid
    if height >= m:
        start = mid+1
    else:
        end = mid-1
print(end)