from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.tree = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.tree.append(node.val)
                inorder(node.right)

        inorder(root)

    def next(self) -> int:
        return self.tree.pop(0)

    def hasNext(self) -> bool:
        return bool(self.tree)  # if self.tree
