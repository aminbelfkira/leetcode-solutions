# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Accepted: 2026-09-30T21:55:50.000Z
# Language: Python3
# Runtime: 43 ms · Beats 83.14%
# Memory: 20 MB · Beats 89.15%
# Submission: https://leetcode.com/submissions/detail/2158617704/

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
        old_to_new = {}
        current = head
        while current : 
            old_to_new[current] = Node(current.val)
            current= current.next
        
        current = head 
        while current : 
            old_to_new[current].next = old_to_new.get(current.next, None)
            old_to_new[current].random = old_to_new.get(current.random, None)
            current= current.next
        return old_to_new.get(head, None)
        
