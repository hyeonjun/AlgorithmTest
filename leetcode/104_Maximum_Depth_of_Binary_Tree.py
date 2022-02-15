class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global answer
        answer = 0
        def dfs(root, depth):
            global answer
            if not root:
                return
            answer = max(answer, depth)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 1)
        return answer
