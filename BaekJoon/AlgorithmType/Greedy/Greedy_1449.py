n, l = map(int, input().split())
arr = sorted(map(int, input().split()))
start, end = arr[0], arr[0]+l
answer = 1
for i in range(n):
    if start <= arr[i] < end:
        continue
    else:
        answer += 1
        start, end = arr[i], arr[i]+l
print(answer)
