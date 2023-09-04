import os
import copy
import math
import numpy as np
import itertools

def updateStr (S, Q, pos):
    if pos == 0: return Q + S [1:]
    else: return S [0:pos] + Q + S [pos + 1:]

class Hashed:

    def __init__ (self, N):
        self.N = N
        self.rows = np.zeros (  N    , dtype = int)
        self.cols = np.zeros (  N    , dtype = int)
        self.offd = np.zeros (2*N - 1, dtype = int)
        self.diag = np.zeros (2*N - 1, dtype = int)

    def canPlaceQueen (self, r, c):
        d, o = self.N - 1 - c + r, r + c
        return (self.rows [r] + self.cols [c] + self.diag [d] + self.offd [o]) == 0

    def findAllPossible (self):
        rows = np.where (self.rows == 0) [0].tolist ()
        cols = np.where (self.cols == 0) [0].tolist ()
        return list (filter (lambda rc: self.canPlaceQueen (*rc), itertools.product (rows, cols)))

    def placeQueen (self, r, c):
        self.rows [r] = 1
        self.cols [c] = 1
        self.offd [r + c] = 1
        self.diag [self.N - 1 - c + r] = 1

    def removeQueen (self, r, c):
        self.rows [r] = 0
        self.cols [c] = 0
        self.offd [r + c] = 0
        self.diag [self.N - 1 - c + r] = 0

class Mirror:

    def __init__ (self, board, N):
        self.board, self.N = board, N

    @staticmethod
    def alongX (board): return list (reversed (board))

    
    @staticmethod
    def alongY (board): return [ list (reversed (line)) for line in board ]

    @staticmethod
    def alongD (board, N):
        rev = np.empty ((N, N), dtype = str)
        for r in range (N):
            for c in range (N):
                rev [c] [r] = board [r] [c]
        return [ ''.join (line) for line in rev ]

    def combineAll (self):
        solutions = {}
        for i in range (8):
            board = copy.deepcopy (self.board)
            if i // 4 == 0:     board = self.alongX (board)
            if i % 4 // 2 == 0: board = self.alongY (board)
            if i % 2 == 0:      board = self.alongD (board, self.N)
            board = [ ''.join (line) for line in board ]
            solutions [os.linesep.join (board)] = board
        return solutions

class Solution:

    def placeQueenBoard (self, board, r, c):
        board [r] [c] = 'Q'
        self.hashed.placeQueen (r, c)

    def removeQueenBoard (self, board, r, c):
        board [r] [c] = '.'
        self.hashed.removeQueen (r, c)

    def backtrack_v1 (self, board, N, i):
        if i == N:
            self.solutions [os.linesep.join (board)] = list (board)
            return
        choices = self.hashed.findAllPossible ()
        for (r, c) in choices:
            self.placeQueenBoard (board, r, c)
            self.backtrack_v1 (board, N, i + 1)
            self.removeQueenBoard (board, r, c)

    def backtrack_v2 (self, board, N, r):
        if r == N:
            self.solutions.append ([ ''.join (line) for line in board ])
            return
        for c in range (N):
            if not self.hashed.canPlaceQueen (r, c): continue
            self.placeQueenBoard (board, r, c)
            self.backtrack_v2 (board, N, r + 1)
            self.removeQueenBoard (board, r, c)

    def solveNQueens (self, N: int) -> List[List[str]]:
        self.hashed = Hashed (N)
        board = [ ['.'] * N for _ in range (N) ]
        self.solutions = []
        self.backtrack_v2 (board, N, 0)
        return self.solutions
