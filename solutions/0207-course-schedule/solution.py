# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted: 2026-09-30T22:36:14.000Z
# Language: Python3
# Runtime: 7 ms · Beats 44.2%
# Memory: 20.5 MB · Beats 53.54%
# Submission: https://leetcode.com/submissions/detail/2158629335/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        inorder = [0] * numCourses
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for course, prereq in prerequisites : 
            graph[prereq].append(course)
            inorder[course] +=1
        
        queue = deque([i for i in range(numCourses) if inorder[i]== 0])
        visited = set()
        while queue :
            current = queue.popleft()
            visited.add(current)
            for neighbor in graph[current] : 
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0 : 
                    queue.append(neighbor)
        
        return len(visited) == numCourses

