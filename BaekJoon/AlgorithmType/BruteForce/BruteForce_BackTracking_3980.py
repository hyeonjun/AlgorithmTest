def dfs(idx, arr):
    global answer
    if idx == 11:
        answer = max(answer, sum(arr))
        return

    for j in range(11): # 포지션
        if arr[j] or not player[idx][j]:
            continue
        arr[j] = player[idx][j]
        dfs(idx+1, arr)
        arr[j] = 0

for _ in range(int(input())):
    player = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    dfs(0, [0 for _ in range(11)])
    print(answer)