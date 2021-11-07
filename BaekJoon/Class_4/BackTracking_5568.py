n = int(input())
k = int(input())
num = [int(input()) for _ in range(n)]

answer = set()
tmp = []
visited = [False for _ in range(n)]

def dfs():
    if len(tmp) == k:
        answer.add(''.join(map(str, tmp)))
        return
    for i in range(n):
        if not visited[i]:
            tmp.append(num[i])
            visited[i] = True
            dfs()
            visited[i] = False
            tmp.pop()
dfs()
print(len(answer))