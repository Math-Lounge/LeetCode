# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    @staticmethod
    def swapValues (lhs, rhs):
        lhs.val, rhs.val = rhs.val, lhs.val

    @classmethod
    def swapNextNodes (cls, lhs, rhs, repeat):
        lhs.next, rhs.next = rhs.next, lhs.next
        if not repeat: return
        cls.swapNextNodes (lhs.next, rhs.next, False)

    def swapNodes (self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node, lhs = head, None
        i, cache = 1, [ None for _ in range (k) ]
        while node is not None:
            cache [i % k] = node
            if (i == k): lhs = node
            node = node.next
            i += 1
        # Now i is set to the k-th from back node
        self.swapValues (lhs, cache [i % k])
        return head
