# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Accepted: 2026-09-18T12:38:37.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 65.53%
# Submission: https://leetcode.com/submissions/detail/2145730098/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left-1) : 
            prev = prev.next
        current = prev.next
        for _ in range(right - left) : 
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
            
        return dummy.next
