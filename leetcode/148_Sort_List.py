# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, left, right):
        dummy = tail = ListNode(None)
        while left and right:
            if left.val < right.val:
                tail.next, tail, left = left, left, left.next
            else:
                tail.next, tail, right = right, right, right.next
        tail.next = left or right
        return dummy.next
