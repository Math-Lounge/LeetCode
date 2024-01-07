import heapq

class Solution:

    @staticmethod
    def distance (points, i, j):
        return sum \
        ([
            abs (points [i] [0] - points [j] [0]),
            abs (points [i] [1] - points [j] [1]),
        ])

    def minCostConnectPoints (self, points: List[List[int]]) -> int:
        N = len (points)
        visited = [ False for _ in range (N) ]
        heap = [(0,0)] # weight, node_num
        mst_cost = 0
        while sum (visited) != N:
            node_cost, node = heapq.heappop (heap)
            if visited [node]: continue
            mst_cost += node_cost
            visited [node] = True
            for neighbor in range (N):
                if visited [neighbor]: continue # also covers self
                weight = self.distance (points, node, neighbor)
                heapq.heappush (heap, (weight, neighbor))
        return mst_cost
