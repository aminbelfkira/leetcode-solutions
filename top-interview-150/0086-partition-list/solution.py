# 86. Partition List
# https://leetcode.com/problems/partition-list/
# Accepted: 2026-09-06T11:54:12.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 39.42%
# Submission: https://leetcode.com/submissions/detail/2132801759/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        before_dummy = ListNode(next = head)
        after_dummy = ListNode(next = head)
        before = before_dummy
        after = after_dummy
        current = head

        while current :
            val = current.val
            if val <x : 
                before.next = current
                before = before.next
            else : 
                after.next = current
                after = after.next
            current = current.next
        
        after.next = None
        before.next = after_dummy.next

        return before_dummy.next

