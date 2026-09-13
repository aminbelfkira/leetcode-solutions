# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Accepted: 2026-09-13T21:26:07.000Z
# Language: Python3
# Runtime: 3 ms · Beats 27.91%
# Memory: 19.4 MB · Beats 7.2%
# Submission: https://leetcode.com/submissions/detail/2141026211/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        while current : 
            if current.next and current.next.val == current.val : 
                value = current.val 
                while current and current.val == value : 
                    current = current.next
                prev.next = current
            else : 
                prev = current
                current = current.next
        return dummy.next
