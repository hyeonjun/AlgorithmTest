# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start, end = head, head
        idx = 1
        pointer = head

        while pointer.next:
            pointer = pointer.next
            # 앞에서부터 k번째 수를 찾는다
            if idx < k:
                idx += 1
                start = start.next
            else: # start를 찾은 후 남은 수 만큼 움직이면 뒤에서 k번째를 수를 찾을 수 있다
                end = end.next

        start.val, end.val = end.val, start.val
        return head
