n = int(input())
graph = {}
parent = [False] * (n+1)
parent[0] = True
for _ in range(n):
    node, left, right = map(int, input().split())
    if left != -1:
        parent[left] = True
    if right != -1:
        parent[right] = True
    graph[node] = {'left': left, 'right': right}


def inOrder(node, level):
    global idx
    left, right = graph[node]['left'], graph[node]['right']
    if left != -1:
        inOrder(left, level+1)
    nodeLevel[level].append(idx)
    idx += 1
    if right != -1:
        inOrder(right, level+1)

nodeLevel = [[] for _ in range(n+1)]
root, idx = parent.index(False), 1
inOrder(root, 1)
ansWidth, ansLevel = 0, 0

for level, node in enumerate(nodeLevel[1:]):
    if node:
        width = node[-1] - node[0] + 1
        if ansWidth < width:
            ansWidth = width
            ansLevel = level+1
print(ansLevel, ansWidth)