n = int(input())
arr = list(map(int, input().split()))
index = list(range(1, n+1))
move = arr.pop(0)
position = 0
answer = [index.pop(0)]
while arr:
    if move < 0:
        position = (position + move) % len(arr)
    else:
        position = (position + move - 1) % len(arr)
    move = arr.pop(position)
    answer.append(index.pop(position))
print(*answer)
