# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root) -> int:
        def solution(node, low, high):
            if not node:
                return high - low
            left = solution(node.left, low, node.val)
            right = solution(node.right, node.val, high)
            return min(left, right)  # find minimum Difference

        return solution(root, float('-inf'), float('inf'))

class Solution:
    def __init__(self):
        self.pre = float('-inf')
        self.ans = float('inf')
    def getMinimumDifference(self, root) -> int:
        if not root:
            return
        self.getMinimumDifference(root.left)
        self.ans = min(self.ans, root.val - self.pre)
        self.pre = root.val
        self.getMinimumDifference(root.right)
        return self.ans