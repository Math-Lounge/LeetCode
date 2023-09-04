class Solution:

    def jump (self, nums: List[int]) -> int:
        furthest = jump_end = hop_count = 0
        for i in range (len (nums) - 1):
            furthest = max (furthest, i + nums [i])
            if i == jump_end:
                hop_count += 1
                jump_end = furthest
        return hop_count
