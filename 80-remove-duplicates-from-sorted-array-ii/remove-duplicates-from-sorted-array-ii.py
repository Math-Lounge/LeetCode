class Solution:
    def removeDuplicates (self, nums: List[int]) -> int:
        wi = 2
        for ri in range (2, len (nums)):
            if nums [wi-2] != nums [ri]:
                nums [wi] = nums [ri]
                wi += 1
        return wi
