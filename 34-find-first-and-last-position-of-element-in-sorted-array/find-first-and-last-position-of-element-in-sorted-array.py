class Solution:

    def search (self, nums, target, dir_left):
        L, R, i = 0, len (nums) - 1, -1
        while (L <= R):
            m  = (L+R) // 2
            if   (target  == nums [m]):
                i = m
                if dir_left: R = m-1
                else       : L = m+1
            elif (target   < nums [m]): R = m-1
            elif (nums [m] < target  ): L = m+1
        return i

    def searchRange (self, nums: List[int], target: int) -> List[int]:
        L = self.search (nums, target, True)
        if L == -1: return [-1,-1]
        R = self.search (nums, target, False)
        return [L,R]
