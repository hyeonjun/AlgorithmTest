class Solution:
    def connect(self, root):
        if not root:
            return root
        queue = [root]
        tail = root
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node == tail:
                node.next = None
                tail = queue[-1] if queue else None
            else:
                node.next = queue[0]
        return root