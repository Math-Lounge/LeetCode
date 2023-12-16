class Solution:
    def findMissingRanges (self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        return self._findMissingRanges_ ([lower-1] + nums + [upper+1])

    def _findMissingRanges_ (self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range (1, len (nums)):
            if nums [i] != nums [i-1] + 1:
                output.append ([ nums [i-1] + 1, nums [i] - 1 ])
        return output
