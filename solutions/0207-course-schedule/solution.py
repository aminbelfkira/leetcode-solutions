# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted: 2026-09-14T19:56:30.000Z
# Language: Python3
# Runtime: 6 ms · Beats 49.27%
# Memory: 20.3 MB · Beats 78.99%
# Submission: https://leetcode.com/submissions/detail/2141969508/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 
        graph = defaultdict(list)
        indegree= [0] * numCourses
        for course, prereq in prerequisites : 
            graph[prereq].append(course)
            indegree[course]+=1
        
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        visited = 0
        while queue :
            node= queue.popleft()
            visited +=1
            for nxt in graph[node] : 
                indegree[nxt] -= 1
                if indegree[nxt] == 0 :
                    queue.append(nxt)
        return visited == numCourses
