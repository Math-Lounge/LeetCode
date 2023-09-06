class Solution:
    def getRow (self, rowIndex: int) -> List[int]:
        last = [1]
        if rowIndex == 0: return last
        for r in range (1, rowIndex+1):
            curr = [1] * (r+1)
            for c in range (1, r):
                curr [c] = last [c-1] + last [c]
            last = curr
        return last
