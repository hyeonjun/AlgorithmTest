n = int(input())
strs = input()
S = [[0 for _ in range(n)] for _ in range(n)]
k = 0
for i in range(n):
    for j in range(i, n):
        if strs[k] == '+':
            S[i][j] = 1
        elif strs[k] == '-':
            S[i][j] = -1
        k += 1
answer = []

def check(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += answer[i]
        if s == 0 and S[i][idx] != 0:
            return False
        elif s < 0 and S[i][idx] > 0:
            return False
        elif s > 0 and S[i][idx] < 0:
            return False
    return True
endPoint = False
def dfs(idx):
    global endPoint
    if idx == n:
        endPoint = True
        return
    for i in range(1, 11):
        answer.append(S[idx][idx] * i)
        if check(idx):
            dfs(idx+1)
        if endPoint:
            break
        answer.pop()
dfs(0)
print(*answer)