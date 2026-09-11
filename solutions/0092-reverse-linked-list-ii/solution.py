# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Accepted: 2026-09-11T17:45:03.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 25.49%
# Submission: https://leetcode.com/submissions/detail/2138827344/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        k = 0
        for _ in range(left -1) : 
            prev = prev.next
        current = prev.next
        for _ in range(right -left ) : 

            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next
