# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Accepted: 2026-09-12T12:54:26.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 55 ms · Beats 33.82%
# Memory: 20.4 MB · Beats 27.25%
# Submission: https://leetcode.com/submissions/detail/2139494160/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        from collections import deque

        queue = deque([root])
        while queue : 
            level_size = len(queue)
            prev = None
            for _ in range(level_size) : 
                current = queue.popleft()
                if current : 
                    queue.append(current.right)
                    queue.append(current.left)
                    current.next = prev
                    prev = current
        return root
