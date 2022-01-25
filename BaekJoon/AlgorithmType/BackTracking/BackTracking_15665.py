# set, 916ms
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = set()
def dfs(depth, lst):
    if depth == m:
        answer.add(tuple(lst))
        return
    for i in range(n):
        lst.append(arr[i])
        dfs(depth+1, lst)
        lst.pop()
dfs(0, [])
for a in sorted(answer):
    print(*a)

# 404ms
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
def dfs(depth, lst):
    if depth == m:
        print(*lst)
        return
    prev = 0
    for i in range(n):
        if prev != arr[i]:
            lst.append(arr[i])
            prev = arr[i]
            dfs(depth+1, lst)
            lst.pop()
dfs(0, [])