class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        L, R = 0, len (nums) - 1
        while (L < R):
            T = nums [L] + nums [R]
            if (T == target): return [L+1, R+1]
            elif (T < target): L += 1
            elif (T > target): R -= 1
        return [-1]
