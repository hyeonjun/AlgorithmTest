# 트리 순회
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def solution(node_list):
    tree = {}
    for i in node_list:
        tree[i] = Node(i, node_list[i][0], node_list[i][1])

    # n = int(input())
    # tree = {}
    # for i in range(n):
    #     data, left, right = input().split()
    #     tree[data] = Node(data, left, right)

    pre_list = []
    in_list = []
    post_list = []

    def pre_order(node): # root -> left -> right
        pre_list.append(node.data)
        if node.left != '.':
            pre_order(tree[node.left])
        if node.right != '.':
            pre_order((tree[node.right]))

    def in_order(node): # left -> root -> right
        if node.left != '.':
            in_order(tree[node.left])
        in_list.append(node.data)
        if node.right != '.':
            in_order(tree[node.right])

    def post_order(node): # elft -> right -> root
        if node.left != '.':
            post_order(tree[node.left])
        if node.right != '.':
            post_order(tree[node.right])
        post_list.append(node.data)

    pre_order(tree['A'])
    in_order(tree['A'])
    post_order(tree['A'])
    return pre_list, in_list, post_list



# pre_order, in_order, post_order = solution()
# print(''.join(pre_order))
# print(''.join(in_order))
# print(''.join(post_order))

tree = {'A':['B','C'], 'B':['D', '.'], 'C':['E','F'], 'E':['.','.'],'F':['.','G'],'D':['.','.'],'G':['.','.']}

pre_order, in_order, post_order = solution(tree)
print(''.join(pre_order))
print(''.join(in_order))
print(''.join(post_order))
# ==============================================================================

# 트리 높이와 너비
class Node:
    def __init__(self, number, left, right):
        self.parent = -1
        self.number = number
        self.left = left
        self.right = right

def solution(n, node_list):
    global level_depth, x
    level_depth = 1
    level_min = [n]
    level_max = [0]
    root = -1
    x = 1

    # 중위 순회가 x축을 기준으로 왼쪽부터 방문한다는 특징이 있다.
    # 그래서 이 문제는 중위 순회 알고리즘을 이용하여 풀어야한다.
    def in_order(node, level): # 중위 순회 : left -> root -> right
        global level_depth, x
        level_depth = max(level_depth, level)
        if node.left != -1: # 왼쪽
            in_order(tree[node.left], level +1)

        # 현재 레벨에 대해서 가장 작은 값을 찾음
        level_min[level] = min(level_min[level], x)
        # 현재 레벨에 대해서 가장 큰 값을 찾음
        level_max[level] = max(level_max[level], x)
        x += 1

        if node.right != -1: # 오른쪽
            in_order(tree[node.right], level+1)

    tree = {}
    for i in range(1, n+1):
        tree[i] = Node(i, -1, -1)
        level_min.append(n)
        level_max.append(0)

    for i in node_list:
        tree[i].left = node_list[i][0]
        tree[i].right = node_list[i][1]
        if node_list[i][0] != -1:
            tree[node_list[i][0]].parent = i
        if node_list[i][1] != -1:
            tree[node_list[i][1]].parent = i

    for i in range(1, n+1):
        if tree[i].parent == -1:
            root = i

    in_order(tree[root], 1)

    depth = [0] * (n+1)
    depth[1] = 1

    result_level = 1
    result_width = level_max[1] - level_min[1] + 1
    for i in range(2, level_depth+1):
        width = level_max[i] - level_min[i] +1
        depth[i] = width
        if result_width < width:
            result_level = i
            result_width = width

    print(level_min)
    print(level_max)
    print(depth)

    return result_level, result_width

node_list ={
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, -1],
    5: [9, 10],
    6: [11, 12],
    7: [13, -1],
    8: [-1, -1],
    9: [14, 15],
    10: [-1, -1],
    11: [16, -1],
    12: [-1, -1],
    13: [17, -1],
    14: [-1, -1],
    15: [18, -1],
    16: [-1, -1],
    17: [-1, 19],
    18: [-1, -1],
    19: [-1, -1]
}
print(solution(19, node_list))
