import numpy as np

class Solution:

    def maximalNetworkRank (self, n: int, roads: List[List[int]]) -> int:
        graph = np.zeros ((n,n), dtype = bool)
        for (r,c) in roads:
            graph [r,c] = True
            graph [c,r] = True
        network_rank = 0
        for r in range (n):
            for c in range (r+1, n):
                rc_rank = sum (graph [r, :]) + sum (graph [:, c]) - graph [r, c]
                network_rank = max (network_rank, rc_rank)
        print (graph.astype (int))
        return network_rank
