class Solution:

    # path[level] = min(tri[level,:])
    # tri[i,j] = tri[i,j].value + min(tri[i-1,j], tri[i-1,j-1], tri[i-1,j+1])

    def minimumTotal (self, triangle: List[List[int]]) -> int:
        N = len (triangle)
        last = triangle [0]
        for level in range (1, N):
            path = [0] * (level+1)
            path [0]     = triangle [level] [0]     + last [0]       # Direct down
            path [level] = triangle [level] [level] + last [level-1] # Slide right
            for cell in range (1, level):
                path [cell] = triangle [level] [cell] + min (last [cell-1], last [cell])
            last = path
        return min (last)
