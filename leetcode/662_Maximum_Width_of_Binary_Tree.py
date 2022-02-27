class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        answer = 0
        queue = [(root, 0)]
        while queue:
            answer = max(answer, queue[-1][1]-queue[0][1]+1)
            for _ in range(len(queue)):
                node, width = queue.pop(0)
                print(width)
                if node.left:
                    queue.append((node.left, 2 * width))
                if node.right:
                    queue.append((node.right, 2 * width + 1))
        return answer