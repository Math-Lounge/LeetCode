class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.solutions = []
        self._subset_ (nums, 0, [])
        return self.solutions

    def _subset_(self, nums, idx, curr):
        if idx == len (nums):
            self.solutions.append (list (curr))
            return
        self._subset_ (nums, idx + 1, curr)
        curr.append (nums [idx])
        self._subset_ (nums, idx + 1, curr)
        curr.pop (-1)
