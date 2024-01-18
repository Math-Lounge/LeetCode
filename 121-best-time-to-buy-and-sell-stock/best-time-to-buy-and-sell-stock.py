
class Solution:

    def maxProfit (self, prices: List [int]) -> int:

        N = len( prices )
        min_LHS = [ -1 for _ in range( N ) ]
        max_RHS = [ -1 for _ in range( N ) ]
        min_LHS[  0 ] = prices[  0 ]
        max_RHS[ -1 ] = prices[ -1 ]
        profit = -1

        for i in range( 1, N ):
            min_LHS[ i ] = min( min_LHS[ i-1 ], prices[ i ] )
        for i in reversed( range( N-1 ) ):
            max_RHS[ i ] = max( max_RHS[ i+1 ], prices[ i ] )
        for i in range( N ):
            profit = max( profit, max_RHS[ i ] - min_LHS[ i ] )

        return profit
