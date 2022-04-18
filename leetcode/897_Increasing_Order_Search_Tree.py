# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        answer = dummy = TreeNode()
        def inorder(node):
            nonlocal dummy
            if node:
                inorder(node.left)
                dummy.right = TreeNode(node.val)
                dummy = dummy.right
                inorder(node.right)
        inorder(root)
        return answer.right