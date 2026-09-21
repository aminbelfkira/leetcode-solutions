# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Accepted: 2026-09-21T13:00:42.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 91.97%
# Submission: https://leetcode.com/submissions/detail/2148646850/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        fast =head
        for _ in range(n) : 
            fast = fast.next
        current = dummy
        while fast : 
            fast = fast.next
            current = current.next
        current.next = current.next.next

        return dummy.next
