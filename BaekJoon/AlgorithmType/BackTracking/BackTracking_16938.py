n, l, r, x = map(int, input().split())
# n 문제수, l <= 난이도 합 <= r, x <= max(난이도)-min(난이도)
problems = list(map(int, input().split()))
answer = 0
def dfs(idx, cnt, sumP, maxP, minP):
    global answer
    if cnt > 1:
        if l <= sumP <= r and x <= maxP - minP:
            answer += 1

    for i in range(idx, n):
        if problems[i] + sumP <= r:
            dfs(i+1, cnt+1, sumP+problems[i], max(maxP, problems[i]), min(minP, problems[i]))

dfs(0, 0, 0, -1e9, 1e9)
print(answer)