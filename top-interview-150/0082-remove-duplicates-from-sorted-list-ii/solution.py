# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Accepted: 2026-09-06T11:42:25.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 7.02%
# Submission: https://leetcode.com/submissions/detail/2132791993/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)

        current = head
        prev = dummy
        while current :
            if current.next and current.next.val == current.val : 
                val=current.val
                while current and current.val == val:  
                    current = current.next
                    prev.next = current
            else :
                prev = current
                current = current.next
        return dummy.next
