# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Accepted: 2026-09-06T11:04:13.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 92.08%
# Submission: https://leetcode.com/submissions/detail/2132759150/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        prev = dummy
        for _ in range(left -1) : 
            prev = prev.next
        curr = prev.next
        for _ in range(right - left) :
            temp = curr.next  ##on stock le prochain
            curr.next = temp.next 
            temp.next = prev.next 
            prev.next = temp
        
        return dummy.next
