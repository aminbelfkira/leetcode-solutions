# 86. Partition List
# https://leetcode.com/problems/partition-list/
# Accepted: 2026-09-11T20:57:48.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 39.32%
# Submission: https://leetcode.com/submissions/detail/2138967958/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        before_dummy = ListNode()
        after_dummy = ListNode()
        before = before_dummy
        after = after_dummy

        current = head 
        while current : 
            if current.val < x : 
                before.next = current
                before = before.next
            else : 
                after.next = current
                after = after.next
            current = current.next
        after.next = None
        before.next = after_dummy.next
        return before_dummy.next
