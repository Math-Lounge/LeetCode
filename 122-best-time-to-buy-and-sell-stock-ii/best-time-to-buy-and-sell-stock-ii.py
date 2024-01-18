class Solution:

    def maxProfit( self, prices: List[ int ] ) -> int:

        profit = 0
        N = len( prices )
        for i in range( 1, N ):
            profit += max( 0, prices[ i ] - prices[ i-1 ] )
        return profit
