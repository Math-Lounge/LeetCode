class MinStack:

    def __init__ (self):
        self.min = [] # (min value, count) tuple
        self.stack = []

    def push (self, val) -> None:
        if (len (self.min) == 0):
            self.min.append ((val, 1))
        elif (val < self.min [-1] [0]):
            self.min.append ((val, 1))
        elif (val == self.min [-1] [0]):
            count = self.min.pop () [1]
            self.min.append ((val, count + 1))
        self.stack.append (val)

    def pop (self) -> None:
        if len (self.stack) == 0: return
        val = self.stack.pop ()
        if (val == self.min [-1] [0]):
            count = self.min.pop () [1]
            if count > 1:
                self.min.append ((val, count-1))

    def top (self) -> int:
        return self.stack [-1]

    def getMin (self) -> int:
        return self.min [-1] [0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()