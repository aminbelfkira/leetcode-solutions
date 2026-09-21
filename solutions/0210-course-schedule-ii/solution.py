# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted: 2026-09-21T07:58:17.000Z
# Language: Python3
# Runtime: 3 ms · Beats 74.88%
# Memory: 20.4 MB · Beats 75.7%
# Submission: https://leetcode.com/submissions/detail/2148416244/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        indegree = [0]* numCourses
        for course, prereq in prerequisites : 
            graph[prereq].append(course)
            indegree[course]+=1
        visited =0
        res = []
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)

        while queue : 
            current = queue.popleft()
            res.append(current)
            visited +=1
            for nxt in graph[current] : 
                indegree[nxt] -= 1
                if indegree[nxt] == 0 :
                    queue.append(nxt)
        return [] if visited != numCourses else res
