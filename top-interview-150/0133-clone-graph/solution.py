# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Accepted: 2026-09-12T21:45:32.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 48 ms · Beats 68.06%
# Memory: 19.7 MB · Beats 87.61%
# Submission: https://leetcode.com/submissions/detail/2140023720/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None : 
            return None
        
        clones = {node : Node(node.val)}
        queue = deque([node])
        while queue : 
            current = queue.popleft()

            for neighbor in current.neighbors : 
                if neighbor not in clones : 
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[current].neighbors.append(clones[neighbor])
            
        return clones[node]
