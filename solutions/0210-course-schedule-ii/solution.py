# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted: 2026-09-14T20:06:16.000Z
# Language: Python3
# Runtime: 8 ms · Beats 11.09%
# Memory: 20.4 MB · Beats 75.38%
# Submission: https://leetcode.com/submissions/detail/2141975163/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for course, prereq in prerequisites : 
            indegree[course] +=1
            graph[prereq].append(course)
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        res = []
        while queue : 
            current = queue.popleft()
            res.append(current)
            for nxt in graph[current] : 
                indegree[nxt] -=1
                if indegree[nxt] == 0 : 
                    queue.append(nxt)
        return res if len(res) == numCourses else []
