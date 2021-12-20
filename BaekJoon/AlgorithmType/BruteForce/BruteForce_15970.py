arr = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()

answer = 0
for i in range(len(arr)):
    now_i, now_c = arr[i]
    left, right = 1e9, 1e9

    # left
    for j in range(i-1, -1, -1):
        if arr[j][1] == now_c:
            left = now_i - arr[j][0]
            break

    # right
    for j in range(i+1, len(arr)):
        if arr[j][1] == now_c:
            right = arr[j][0] - now_i
            break
    answer += min(left, right)
print(answer)