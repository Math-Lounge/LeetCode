import collections

class Solution:

    def findOrder( self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [ [] for _ in range (numCourses) ]
        indegree = [0] * numCourses

        for (course, prereq) in prerequisites:
            graph [prereq].append (course)
            indegree [course] += 1

        queue = collections.deque ()
        for i, count in enumerate (indegree):
            if count == 0:
                queue.append (i)

        order = []
        while queue:
            i = queue.popleft ()
            connections = graph [i]
            for j in connections:
                indegree [j] -= 1
                if indegree [j] == 0:
                    queue.append (j)
            order.append (i)

        return [] if sum (indegree) != 0 else order
