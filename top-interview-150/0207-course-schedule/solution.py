# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted: 2026-09-12T22:32:32.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 10 ms · Beats 13.94%
# Memory: 20.4 MB · Beats 78.82%
# Submission: https://leetcode.com/submissions/detail/2140039681/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) 
        indegree = [0] * numCourses
        for course, prereq in prerequisites :
            graph[prereq].append(course)
            indegree[course]+=1
        
        queue = deque(c for c in range(numCourses) if indegree[c] ==0)
        visited = 0
        while queue :
            node = queue.popleft()
            visited +=1
            for nxt in graph[node] :
                indegree[nxt] -= 1
                if indegree[nxt] == 0 :
                    queue.append(nxt)
        return visited == numCourses
