class Solution:

    def firstMissingPositive (self, nums: List[int]) -> int:
        N = len (nums)
        one_found = False
        for i in range (N):
            one_found |= nums [i] == 1
            if not (0 < nums [i] <= N):
                # negative or >=N
                nums [i] = 1
        if not one_found: return 1
        for i in range (N):
            x = abs (nums [i]) % N
            nums [x] = -abs (nums [x])
        print (nums)
        for i in range (1, N+1):
            if nums [i % N] > 0:
                return i
        return N+1
