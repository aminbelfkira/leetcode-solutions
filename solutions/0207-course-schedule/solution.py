# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted: 2026-09-21T07:52:15.000Z
# Language: Python3
# Runtime: 3 ms · Beats 85.82%
# Memory: 20.2 MB · Beats 93.4%
# Submission: https://leetcode.com/submissions/detail/2148412526/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites : 
            graph[prereq].append(course)
            indegree[course] +=1
        visited = 0
        queue = deque(c for c in range(numCourses) if indegree[c] == 0 )

        while queue : 
            node = queue.popleft()
            visited +=1
            for neighbor in graph[node] : 
                indegree[neighbor] -=1 
                if indegree[neighbor] == 0 :
                    queue.append(neighbor)
        return visited == numCourses

                    
