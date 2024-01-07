class Solution:

    def backtrack (self, nums, curr):
        if len (curr) == len (nums):
            self.answers.append (curr [:])
        for num in nums:
            if num in curr: continue
            curr.append (num)
            self.backtrack (nums, curr)
            curr.pop ()

    def permute (self, nums: List[int]) -> List[List[int]]:
        self.answers = []
        self.backtrack (nums, [])
        return self.answers
