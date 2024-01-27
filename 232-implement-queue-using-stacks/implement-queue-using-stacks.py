class MyQueue:

    def __init__(self):
        self.reg = []
        self.rev = []

    @staticmethod
    def __swap__(src, dst) -> None:
        while src:
            dst.append(src.pop())

    def __reverse__(self) -> None:
        self.__swap__(self.reg, self.rev)

    def __forward__(self) -> None:
        self.__swap__(self.rev, self.reg)

    def push(self, x: int) -> None:
        self.__reverse__()
        self.reg.append(x)
        self.__forward__()

    def pop(self) -> int:
        return self.reg.pop()

    def peek(self) -> int:
        return self.reg[-1]

    def empty(self) -> bool:
        return len(self.reg) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()