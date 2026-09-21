# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# Accepted: 2026-09-21T07:46:01.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 76.44%
# Submission: https://leetcode.com/submissions/detail/2148408854/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for (a,b), value in zip(equations, values) :
            graph[a].append((b, value))
            graph[b].append((a, 1.0 /value))
        
        def evaluate(start, target) : 
            if start not in graph or target not in graph : 
                return -1.0
            
            queue = deque([(start, 1.0)])
            visited = {start}
            while queue : 
                current, ratio = queue.popleft()
                if current== target : 
                    return ratio 
                for neighbor, weight in graph[current] : 
                    if neighbor not in visited : 
                        visited.add(neighbor)
                        queue.append((neighbor, ratio*weight))
            return -1.0
        return [evaluate(a,b) for a,b in queries]
