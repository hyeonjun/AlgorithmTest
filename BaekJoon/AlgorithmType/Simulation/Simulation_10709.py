h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
answer = [[-1 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'c':
            answer[i][j] = 0
        else:
            if j != 0 and answer[i][j-1] != -1:
                answer[i][j] = answer[i][j-1] + 1
for i in answer:
    print(*i)