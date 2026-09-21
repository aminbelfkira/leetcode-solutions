# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Accepted: 2026-09-21T07:42:01.000Z
# Language: Python3
# Runtime: 44 ms · Beats 87.17%
# Memory: 19.6 MB · Beats 98.09%
# Submission: https://leetcode.com/submissions/detail/2148406351/

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
