class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums [0]
        while True:
            slow = nums [slow]
            fast = nums [nums [fast]]
            if slow == fast: break
            # The break can't go in the loop condition
            # Because it fails the initial value case
        slow = nums [0]
        while slow != fast:
            slow = nums [slow]
            fast = nums [fast]
        return fast
