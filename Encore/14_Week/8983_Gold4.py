m, n, l = map(int, input().split())
shooter = sorted(map(int, input().split()))
# animal = [list(map(int, input().split())) for _ in range(n)]
animal = []
for _ in range(n):
    x, y = map(int, input().split())
    if y > l: continue
    animal.append((x, y))

answer = 0
for x, y in animal:
    left, right = 0, m-1
    while left < right: # 각 동물에 대해 가장 가까운 사대를 찾음
        mid = (left+right) // 2
        if shooter[mid] < x:
            left = mid+1
        else:
            right = mid
    # 동물에 대해 가까운 양쪽 사대에 대해 가능한 경우가 있으면 +1
    if abs(shooter[right]-x)+y <= l or abs(shooter[right-1]-x)+y <= l:
        answer += 1
print(answer)