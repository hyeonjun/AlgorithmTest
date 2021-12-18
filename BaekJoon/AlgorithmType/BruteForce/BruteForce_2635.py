n = int(input())
answer = []
for i in range(n+1):
    tmp = [n, i]
    idx = 2
    while True:
        j = tmp[idx-2] - tmp[idx-1]
        if j < 0:
            break
        tmp.append(j)
        idx += 1
    if len(answer) < len(tmp):
        answer = tmp
print(len(answer))
print(*answer)