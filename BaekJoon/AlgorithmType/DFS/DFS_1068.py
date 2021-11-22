n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def dfs(x):
    arr[x] = -2 # 삭제
    for i in range(n):
        if x == arr[i]:
            dfs(i)
dfs(x)
answer = 0
for i in range(n):
    if arr[i] != -2 and i not in arr: # 리프 노드
        answer += 1
print(answer)