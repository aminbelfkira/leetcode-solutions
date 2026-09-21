# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Accepted: 2026-09-21T12:56:50.000Z
# Language: Python3
# Runtime: 3 ms · Beats 27.82%
# Memory: 19.3 MB · Beats 74.35%
# Submission: https://leetcode.com/submissions/detail/2148643599/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0, head)
        prev = dummy
        current = dummy.next
        while current is not None : 
            if current.next and current.val == current.next.val : 
                val = current.val
                while current and current.val == val: 
                    current = current.next
                prev.next = current
            else : 
                prev = current
                current = current.next
        return dummy.next
