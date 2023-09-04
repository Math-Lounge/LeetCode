class Solution:
    def canJump (self, nums: List[int]) -> bool:
        if len (nums) == 1: return True
        dp = [0] * len (nums)
        dp [0] = nums [0]
        for i in range (1, len (nums)):
            if dp [i-1] > 0:
                dp [i] = max (dp [i-1] - 1, nums [i])
        return dp [-2] > 0
