
class Solution:

    def generate (self, numRows: int) -> List[List[int]]:
        triangle = [ [1,], [1,1,], ]
        if numRows <= 2: return triangle [:numRows]
        for r in range (2, numRows):
            row = [1] * (r+1)
            last = triangle [-1]
            for c in range (1, r):
                row [c] = last [c-1] + last [c]
            triangle.append (row)
        return triangle
