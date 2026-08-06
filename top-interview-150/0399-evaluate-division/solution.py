# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# Accepted: 2026-08-06T10:30:04.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 75.71%
# Submission: https://leetcode.com/submissions/detail/2096532658/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(dict)

        for (a,b), value in zip(equations, values) : 
            graph[a][b] = value
            graph[b][a] = 1/value
        
        def dfs(node, target,  visited) :

            if node not in graph or target not in graph : 
                return -1.0

            if node == target  :
                return 1.0

            visited.add(node)
            for neighbor , weight in graph[node].items() : 
                if neighbor not in visited : 
                    result = dfs(neighbor, target, visited) 
                    if result != -1 : 
                        return weight * result
            return -1.0

        return [dfs(c,d, set()) for c, d in queries]


