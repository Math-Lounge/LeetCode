class Solution:

    def recurse (self, board, row, col, word, i, visited):
        if i == len (word): return True
        if (row,col) in visited: return False
        if not ((0 <= row < self.rows) and (0 <= col < self.cols)): return False
        if board [row] [col] != word [i]: return False
        visited.add ((row,col))
        for (r,c) in [ (row, col-1), (row, col+1), (row-1,col), (row+1,col), ]:
            found = self.recurse (board, r, c, word, i+1, visited)
            if found: return True
        visited.remove ((row,col))
        return False

    def exist (self, board: List [List [str]], word: str) -> bool:
        self.rows, self.cols = len (board), len (board [0])
        for r, line in enumerate (board):
            for c, L in enumerate (line):
                found = self.recurse (board, r, c, word, 0, set ())
                if found: return True
        return False
