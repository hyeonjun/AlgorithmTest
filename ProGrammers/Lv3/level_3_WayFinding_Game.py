import sys

sys.setrecursionlimit(10 ** 6)


class Tree:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.left = None
        self.right = None


def solution(nodeinfo):
    pre_list = []
    post_list = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    root = None
    for node in nodeinfo:
        if not root:
            root = Tree(node[0], node[1], node[2])  # x, y, data
        else:
            current = root
            x, y, data = node[0], node[1], node[2]
            while True:
                if current.x > x:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(x, y, data)
                if current.x < x:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(x, y, data)
                break

    def pre_order(node):  # root -> left -> right
        pre_list.append(node.data)
        if node.left:
            pre_order(node.left)
        if node.right:
            pre_order(node.right)

    def post_order(node):  # left -> right -> root
        if node.left:
            post_order(node.left)
        if node.right:
            post_order(node.right)
        post_list.append(node.data)

    pre_order(root)
    post_order(root)
    return [pre_list, post_list]

#  전위                 후위
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))