import collections

class Solution:

    def canFinish (self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        nodes = [ [] for _ in range (numCourses) ]
        indegree = [0] * numCourses
        for (course, prereq) in prerequisites:
            nodes [prereq].append (course)
            indegree [course] += 1

        queue = collections.deque ()
        for i, count in enumerate (indegree):
            if count == 0:
                queue.append (i)

        while queue:
            i = queue.popleft ()
            connections = nodes [i]
            for j in connections:
                indegree [j] -= 1
                if indegree [j] == 0:
                    queue.append (j)

        return sum (indegree) == 0
