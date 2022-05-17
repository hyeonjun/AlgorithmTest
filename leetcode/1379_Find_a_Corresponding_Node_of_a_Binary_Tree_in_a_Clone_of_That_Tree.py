# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS - InOrder
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        global answer

        def inorder(o, c):
            global answer
            if o:
                inorder(o.left, c.left)
                if o is target:
                    answer = c
                    return
                inorder(o.right, c.right)

        inorder(original, cloned)
        return answer

# BFS
from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_o, queue_c = deque([original]), deque([cloned])
        while queue_o:
            no, nc = queue_o.popleft(), queue_c.popleft()
            if no is target:
                return nc
            if no:
                queue_o.extend([no.left, no.right])
                queue_c.extend([nc.left, nc.right])