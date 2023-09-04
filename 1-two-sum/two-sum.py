class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,x in enumerate (nums):
            if (target-x) in hash:
                return [ i, hash [target-x], ]
            else:
                hash [x] = i
        return [-1]
