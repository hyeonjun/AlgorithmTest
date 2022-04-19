# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node)
            dfs(node.right)

        dfs(root)

        sorted_result = sorted(result, key=lambda x: x.val)
        for i in range(len(result)):
            if result[i] != sorted_result[i]:
                result[i].val, sorted_result[i].val = sorted_result[i].val, result[i].val
                break

class Solution2:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.a = self.b = None
        self.prev = None
        self.flag = False

        def dfs(node):
            if not node or self.flag:
                return

            dfs(node.left)
            if self.prev and self.prev.val > node.val:
                if self.a:
                    self.b = node
                    self.flag = True
                else:
                    self.a = self.prev
                    self.b = node
            self.prev = node
            dfs(node.right)

        dfs(root)
        self.a.val, self.b.val = self.b.val, self.a.val