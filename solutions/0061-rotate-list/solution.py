# 61. Rotate List
# https://leetcode.com/problems/rotate-list/
# Accepted: 2026-09-30T21:59:30.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 77.86%
# Submission: https://leetcode.com/submissions/detail/2158618960/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        n = 0
        if not head : 
            return head
        current = head 
        prev = None
        while current : 
            n+=1
            prev = current
            current = current.next

        prev.next = head

        current = head
        prev = None
        for _ in range(n - k%n) : 
            prev = current
            current = current.next
        prev.next = None
        return current
