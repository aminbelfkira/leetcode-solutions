# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Accepted: 2026-09-13T21:53:19.000Z
# Language: Python3
# Runtime: 38 ms · Beats 99.04%
# Memory: 20.4 MB · Beats 27.15%
# Submission: https://leetcode.com/submissions/detail/2141036229/

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
            prev = None
            for _ in range(len(queue)) : 
                current = queue.popleft()
                if current : 
                    current.next = prev
                    prev = current
                    queue.append(current.right)
                    queue.append(current.left)
        return root
