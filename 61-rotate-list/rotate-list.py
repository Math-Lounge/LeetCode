# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    @staticmethod
    def nextNode (node, head):
        return head if node.next is None else node.next

    def rotateRight (self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head) or (not head.next) or (k == 0): return head
        tail, n = head, 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        k %= n
        tail = head
        for i in range (n - k - 1):
            tail = tail.next
        tail.next, head = None, tail.next
        return head

    def rotateRightCopy (self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head) or (not head.next) or (k == 0): return head
        queue = [ None for _ in range (k) ]
        node = head
        for i in range (k):
            queue [i] = node.val
            node = self.nextNode (node, head)
        i, last = 0, node
        while (i == 0) or (last != node):
            node.val, queue [i % k] = queue [i % k], node.val
            node = self.nextNode (node, head)
            i += 1
        return head
