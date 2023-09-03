# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None): return head
        new_head = head.next
        self._swapPairs_ (head, None)
        return new_head

    def _swapPairs_(self, head, prev):
        if (head is None) or (head.next is None): return
        one_ahead = head.next
        two_ahead = head.next.next
        if (prev is not None): prev.next = one_ahead
        head.next = two_ahead
        one_ahead.next = head
        self._swapPairs_ (two_ahead, head)
