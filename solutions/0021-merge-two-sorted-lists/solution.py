# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted: 2026-09-11T21:47:25.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 94.52%
# Submission: https://leetcode.com/submissions/detail/2138986141/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 and l2 :

            l1_val = l1.val
            l2_val = l2.val

            if l1_val < l2_val : 
                current.next = l1
                l1 = l1.next
            else :
                current.next = l2
                l2 = l2.next
            
            current = current.next
        
        if l1 : 
            current.next = l1
        else : 
            current.next = l2
        
        return dummy.next
