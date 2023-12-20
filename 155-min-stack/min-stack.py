class MinStack:

    def __init__ (self):
        self.min = []
        self.stack = []

    def push (self, val) -> None:
        cmin = val if (len (self.min) == 0) else min (val, self.min [-1])
        self.min.append (cmin)
        self.stack.append (val)

    def pop (self) -> None:
        if len (self.stack) == 0: return
        self.stack.pop ()
        self.min.pop ()

    def top (self) -> int:
        return self.stack [-1]

    def getMin (self) -> int:
        return self.min [-1]

class Old:

    def __init__( self ):
        self.stack = []
        self.min = []

    def push( self, val: int ) -> None:
        self.stack.append( val )
        if ( len( self.min ) == 0 ):
            self.min.append( ( val, 1 ) )
            return
        pmin, count = self.min[ -1 ]
        if   pmin <  val: pass
        elif pmin >  val: self.min.append( ( val, 1 ) )
        elif pmin == val:
            del self.min[ -1 ]
            self.min.append( ( val, count + 1 ) )

    def pop( self ) -> None:
        if ( len( self.stack ) == 0 ): return
        val = self.stack[ -1 ]
        del self.stack[ -1 ]
        pmin, count = self.min[ -1 ]
        if val == pmin:
            del self.min[ -1 ]
            if count > 1: self.min.append( ( val, count - 1 ) )

    def top( self ) -> int:
        return self.stack[ -1 ]

    def getMin( self ) -> int:
        return self.min[ -1 ][ 0 ]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()