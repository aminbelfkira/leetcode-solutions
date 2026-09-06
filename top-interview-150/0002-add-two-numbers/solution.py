# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Accepted: 2026-09-06T10:41:40.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 11.49%
# Submission: https://leetcode.com/submissions/detail/2132739591/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or carry: 

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total//10
            total = total%10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current.next = ListNode(total)
            current = current.next
        return dummy.next

