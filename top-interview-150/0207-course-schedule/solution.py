# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted: 2026-08-06T10:38:45.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 86.11%
# Memory: 21.2 MB · Beats 25.16%
# Submission: https://leetcode.com/submissions/detail/2096542001/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
     ### on va essayer de détecter un cycle

        graph = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites : 
            graph[course].append(prereq)
        
        state = [0] * numCourses

        def dfs(course) : 
            if state[course] ==1 : 
                return False
            if state[course] ==2 : 
                return True
            
            state[course] = 1
            for prereq in graph[course] : 
                if not dfs(prereq) : 
                    return False
            state[course] = 2
            return True
        
        for course in range(numCourses) : 
            if not dfs(course) : 
                return False
        
        return True
