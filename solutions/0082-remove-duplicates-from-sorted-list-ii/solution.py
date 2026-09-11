# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Accepted: 2026-09-11T20:48:38.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 7.02%
# Submission: https://leetcode.com/submissions/detail/2138964175/

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
            if current.next and current.val ==current.next.val : 
                val = current.val
                while current and current.val == val : 
                    current = current.next
                    prev.next = current
            else : 
                prev = current
                current = current.next 
        return dummy.next
        

        
