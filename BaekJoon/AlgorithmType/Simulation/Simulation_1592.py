n, m, l = map(int, input().split())
arr = [0 for _ in range(n)]
idx = 0
answer = 0
while True:
    arr[idx] += 1
    if arr[idx] == m:
        print(answer)
        break
    if arr[idx] % 2 == 1:
        idx = (idx+l) % n
    else:
        idx = (idx-l) % n
    answer += 1