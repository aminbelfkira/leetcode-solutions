# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted: 2026-08-06T10:46:22.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 6 ms · Beats 31.24%
# Memory: 20.2 MB · Beats 90.22%
# Submission: https://leetcode.com/submissions/detail/2096549777/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import deque

        graph = {i : [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course , prereq in prerequisites : 
            graph[prereq].append(course)
            in_degree[course] +=1
        
        queue = deque([c for c in range(numCourses) if in_degree[c]==0])
        order = []

        while queue : 
            course = queue.popleft()
            order.append(course)
            for next_course in graph[course] : 
                in_degree[next_course] -=1
                if in_degree[next_course] == 0 : 
                    queue.append(next_course)

        return order if len(order) == numCourses else []
