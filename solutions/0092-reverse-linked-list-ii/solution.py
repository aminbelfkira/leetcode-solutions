# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Accepted: 2026-09-13T19:38:37.000Z
# Language: Python3
# Runtime: 4 ms · Beats 1.35%
# Memory: 19.6 MB · Beats 25.64%
# Submission: https://leetcode.com/submissions/detail/2140972276/

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
        for _ in range(left -1) :
            prev = prev.next
        curr = prev.next
        print(prev)
        print(curr)
        for _ in range(right -left) : 
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        
        return dummy.next
