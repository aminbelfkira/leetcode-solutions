# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted: 2026-09-06T10:49:13.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 94.65%
# Submission: https://leetcode.com/submissions/detail/2132746068/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        current = dummy
        while l1 and l2 :
            l1_val = l1.val
            l2_val = l2.val

            if l1_val <l2_val : 
                current.next = ListNode(l1_val)
                l1=l1.next
            else : 
                current.next = ListNode(l2_val)
                l2 = l2.next
            current = current.next
        if l1 : 
            current.next = l1
        if l2 : 
            current.next = l2
        
        return dummy.next


            
