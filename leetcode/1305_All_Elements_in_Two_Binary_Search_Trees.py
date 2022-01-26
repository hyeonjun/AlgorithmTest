# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        stack1, stack2 = [], []
        answer = []

        while root1 or root2 or stack1 or stack2:
            # 왼쪽 먼저
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            # stack2가 비어있으면 stack1의 값을 넣어야 하고
            # 비어 있지 않으면 값을 비교해서 stack1의 값이 작으면 answer에 넣음
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                root1 = stack1.pop()
                answer.append(root1.val)
                root1 = root1.right  # 다음 값으로 넘어감
            else:
                root2 = stack2.pop()
                answer.append(root2.val)
                root2 = root2.right
        return answer


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        answer = self.travel(root1) + self.travel(root2)
        return sorted(answer)

    def travel(self, root):
        result = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result


class Solution:
    def __init__(self):
        self.answer = []

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        self.travel(root1)
        self.travel(root2)
        return sorted(self.answer)

    def travel(self, root):
        if not root:
            return
        if root.left:
            self.travel(root.left)
        self.answer.append(root.val)
        if root.right:
            self.travel(root.right)
