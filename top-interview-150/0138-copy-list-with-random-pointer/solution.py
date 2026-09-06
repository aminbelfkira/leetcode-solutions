# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Accepted: 2026-09-06T10:55:18.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 43 ms · Beats 83.35%
# Memory: 20.1 MB · Beats 58.02%
# Submission: https://leetcode.com/submissions/detail/2132751328/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head :
            return None

        new = {}

        current = head
        while current : 
            new[current] = Node(current.val)
            current = current.next
        
        current = head 
        while current : 
            new[current].next = new.get(current.next, None)
            new[current].random = new.get(current.random, None)

            current = current.next
        
        return new[head]
