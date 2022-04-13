k = int(input())
order = list(map(int, input().split()))
n = len(order)
answer = [[] for _ in range(k)]

def dfs(left, right, depth):
    if left == right:
        answer[depth].append(order[left])
        return
    root = (left + right) // 2
    answer[depth].append(order[root])

    dfs(left, root-1, depth+1)
    dfs(root+1, right, depth+1)

dfs(0, n-1, 0)
for ans in answer:
    print(*ans)