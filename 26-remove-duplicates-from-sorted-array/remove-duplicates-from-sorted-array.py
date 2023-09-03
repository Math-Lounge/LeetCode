class Solution:

    def removeDuplicates (self, nums: List[int]) -> int:
        wi = 1
        for ri in range (1, len (nums)):
            if (nums [ri] != nums [wi-1]):
                nums [wi] = nums [ri]
                wi += 1
        return wi
