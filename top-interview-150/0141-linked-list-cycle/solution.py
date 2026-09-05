# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Accepted: 2026-09-05T22:35:05.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 61 ms · Beats 15.17%
# Memory: 22.5 MB · Beats 86.44%
# Submission: https://leetcode.com/submissions/detail/2132192483/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast : 
                return True
        return False 
        
