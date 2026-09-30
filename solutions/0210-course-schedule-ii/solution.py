# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted: 2026-09-30T22:48:06.000Z
# Language: Python3
# Runtime: 3 ms · Beats 74.68%
# Memory: 20.5 MB · Beats 56.77%
# Submission: https://leetcode.com/submissions/detail/2158632460/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        inorder= [0] * numCourses
        for course, prereq in prerequisites :
            graph[prereq].append(course)
            inorder[course] +=1
        
        visited = []
        queue = deque([i for i in range(numCourses) if inorder[i]==0])
        while queue : 
            current = queue.popleft()
            visited.append(current)
            for neighbor in graph[current] : 
                inorder[neighbor] -= 1 
                if inorder[neighbor] == 0 : 
                    queue.append(neighbor)
        return visited if len(visited) == numCourses else []
