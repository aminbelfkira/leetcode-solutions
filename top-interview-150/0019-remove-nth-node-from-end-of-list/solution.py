# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Accepted: 2026-09-06T11:23:22.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 25.27%
# Submission: https://leetcode.com/submissions/detail/2132775939/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode
        dummy.next = head
        fast = head
        for _ in range(n) :
            fast = fast.next
        current= dummy
        while fast : 
            current = current.next
            fast = fast.next
        current.next = current.next.next

        return dummy.next
            
