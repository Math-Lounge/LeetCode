class Solution:

    def threeSum (self, nums: List[int]) -> List[List[int]]:
        nums.sort ()
        N = len (nums)
        results = []
        for i, val in enumerate (nums):
            if val > 0: break
            # Remaining numbers are positive
            # and can't add up to a neg number
            if (i > 0) and (nums [i] == nums [i-1]): continue
            # We have already seen this number before
            self.twoSum (nums, -val, i+1, N-1, results)
        return results

    def twoSum (self, nums, target, L, R, results):
        while L < R:
            S = nums [L] + nums [R]
            if  (S == target):
                results.append ([ -target, nums [L], nums [R], ])
                L, R = L+1, R-1
                # But both L & R could be repeated values
                while (L < R) and (nums [L] == nums [L-1]): L += 1
                while (L < R) and (nums [R] == nums [R+1]): R -= 1
            elif (S < target): L += 1
            elif (S > target): R -= 1
