# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted: 2026-09-12T22:36:14.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 8 ms · Beats 11.07%
# Memory: 20.2 MB · Beats 91.17%
# Submission: https://leetcode.com/submissions/detail/2140040751/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)

        indegree = [0]* numCourses
        for course, prereq in prerequisites : 
            graph[prereq].append(course)
            indegree[course] +=1
        
        queue = deque(c for c in range(numCourses) if indegree[c]==0)
        order = []
        while queue : 
            node = queue.popleft()
            order.append(node)
            for nxt in graph[node] : 
                indegree[nxt] -=1
                if indegree[nxt]==0 : 
                    queue.append(nxt)
        return order if len(order) == numCourses else []
