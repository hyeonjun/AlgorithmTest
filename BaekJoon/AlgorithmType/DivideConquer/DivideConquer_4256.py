"""
preorder: 루트 왼쪽 오른쪽
inorder: 왼쪽 루트 오른쪽
postorder: 왼쪽 오른쪽 루트
"""
def postorder(preorder, inorder):
    if not preorder:
        return
    if len(preorder) == 1:
        result.extend(preorder)
        return

    root = preorder[0]
    idx = inorder.index(root)

    # left
    postorder(preorder[1:idx+1], inorder[:idx])
    # right
    postorder(preorder[idx+1:], inorder[idx+1:])
    result.append(root)

for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    result = []
    postorder(preorder, inorder)
    print(*result)