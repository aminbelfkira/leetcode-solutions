# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Accepted: 2026-10-06T13:06:00.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 74.83%
# Submission: https://leetcode.com/submissions/detail/2164243534/

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
        while current :
            if current.next and current.next.val == current.val : 
                val = current.val
                while current and current.val ==val :
                    current = current.next
                prev.next = current
            else : 
                prev = current
                current = current.next
        return dummy.next
            
