# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Accepted: 2026-09-12T22:26:56.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 64.17%
# Memory: 20.5 MB · Beats 62.41%
# Submission: https://leetcode.com/submissions/detail/2140037938/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prereq in prerequisites : 
            graph[prereq].append(course)
        
        state = [0] * numCourses
        stack = []

        for start in range(numCourses) : 
            if state[start] != 0 : 
                continue
            stack.append((start, iter(graph[start])))
            state[start] = 1

            while stack : 
                node, neighbors = stack[-1]
                advanced = False
                for nxt in neighbors : 
                    if state[nxt] ==1 :
                        return False
                    if state[nxt] == 0 :
                        state[nxt] = 1
                        stack.append((nxt, iter(graph[nxt])))
                        advanced = True
                        break
                if not advanced : 
                    state[node] = 2
                    stack.pop()
        return True
