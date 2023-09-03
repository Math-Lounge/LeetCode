class Solution:

    def removeDuplicates (self, nums: List[int]) -> int:
        wi = 1
        for idx, val in enumerate (nums, 1):
            if (val != nums [wi-1]):
                nums [wi] = val
                wi += 1
        return wi
