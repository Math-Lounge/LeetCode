class Solution:

    def threeSum (self, nums: List[int]) -> List[List[int]]:
        nums.sort ()
        res = []
        for i, val in enumerate (nums):
            if val > 0: break
            if (i == 0) or (val != nums [i-1]):
                self.twoSum (nums, i, res)
        return res

    def twoSum (self, nums, i, res):
        L, R = i+1, len (nums) - 1
        while (L < R):
            T = nums [L] + nums [R] + nums [i]
            if (T == 0):
                res.append ([ nums [i], nums [L], nums [R], ])
                L += 1; R -= 1;
                while (L < R) and (nums [L] == nums [L-1]): L += 1
                while (L < R) and (nums [R] == nums [R+1]): R -= 1
            elif (T < 0): L += 1
            elif (T > 0): R -= 1
