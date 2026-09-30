# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Accepted: 2026-09-30T22:16:20.000Z
# Language: Python3
# Runtime: 49 ms · Beats 59.81%
# Memory: 19.8 MB · Beats 19.47%
# Submission: https://leetcode.com/submissions/detail/2158623917/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None : 
            return None
        clones = {node : Node(node.val)}
        from collections import deque
        queue = deque([node])

        while queue : 
            current = queue.popleft()
            for neighbor in current.neighbors : 
                if neighbor not in clones : 
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[current].neighbors.append(clones[neighbor])
        return clones[node]
