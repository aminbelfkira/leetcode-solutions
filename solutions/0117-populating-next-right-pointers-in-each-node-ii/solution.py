# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Accepted: 2026-09-21T13:05:40.000Z
# Language: Python3
# Runtime: 47 ms · Beats 81.25%
# Memory: 20.3 MB · Beats 90.45%
# Submission: https://leetcode.com/submissions/detail/2148651158/

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

        queue = deque([root]) if root else []

        while queue : 
            prev = None 
            level = len(queue)
            for _ in range(level) : 
                current = queue.popleft()
                current.next = prev
                prev = current
                if current.right : 
                    queue.append(current.right)
                if current.left :
                    queue.append(current.left)
                current = current.next
        
        return root
                
