class Solution:

    def __init__ (self):
        self.memo = { 1: 1, 2: 2, }

    def climbStairs (self, n: int) -> int:
        if n not in self.memo:
            step_1 = self.climbStairs (n-1)
            step_2 = self.climbStairs (n-2)
            self.memo [n] = step_1 + step_2
        return self.memo [n]
