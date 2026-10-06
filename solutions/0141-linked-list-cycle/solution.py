# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Accepted: 2026-10-06T11:51:39.000Z
# Language: Python3
# Runtime: 59 ms · Beats 23.66%
# Memory: 22.7 MB · Beats 28.78%
# Submission: https://leetcode.com/submissions/detail/2164185443/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode(0, head)

        slow = head
        fast = head
        while fast is not None and fast.next is not None : 
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        return False
