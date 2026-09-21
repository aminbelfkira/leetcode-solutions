# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Accepted: 2026-09-21T11:43:54.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 43.12%
# Submission: https://leetcode.com/submissions/detail/2148589881/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 is not None or l2 is not None or carry : 
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val +carry
            carry = total//10
            total = total%10
            current.next = ListNode(total)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return dummy.next
