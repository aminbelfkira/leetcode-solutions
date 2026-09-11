# 61. Rotate List
# https://leetcode.com/problems/rotate-list/
# Accepted: 2026-09-11T20:53:02.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 40.54%
# Submission: https://leetcode.com/submissions/detail/2138965994/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n = 0 
        prev = None
        current = head
        while current : 
            prev = current
            current = current.next
            n+=1
        if n == 0 :
            return head
        k = k %n 
        prev.next = head

        prev = None
        current = head
        for _ in range(n-k) : 
            prev = current
            current = current.next
        
        new_head = current
        prev.next = None
        return new_head
