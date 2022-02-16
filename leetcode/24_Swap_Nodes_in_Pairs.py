# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 이전 노드(pre): 이전 노드가 없으므로 self를 사용
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            x = pre.next
            y = x.next
            # pre -> x -> y -> y.next => pre -> y -> x -> y.next
            pre.next, y.next, x.next = y, x, y.next
            pre = x
        return self.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            x = pre.next
            y = x.next
            # pre -> x -> y -> y.next => pre -> y -> x -> y.next
            pre.next, y.next, x.next = y, x, y.next
            pre = x
        return dummy.next

# Recursive
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(node):
            if not node or not node.next:
                return
            node.val, node.next.val = node.next.val, node.val
            recursive(node.next.next)
        recursive(head)
        return head
