# 61. Rotate List
# https://leetcode.com/problems/rotate-list/
# Accepted: 2026-09-06T11:48:56.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 40.87%
# Submission: https://leetcode.com/submissions/detail/2132797474/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0 :
            return head
        
        n=1
        dummy = ListNode(next= head)
        current = head
        while current.next : 
            current = current.next
            n+=1

        current.next = head ##circular list
        prev = current
        current =head
        k = k%n

        for _ in range(n-k) : 
            prev = current
            current = current.next
        
        prev.next = None

        new_head = current

        return new_head
        
