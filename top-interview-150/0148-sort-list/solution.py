# 148. Sort List
# https://leetcode.com/problems/sort-list/
# Accepted: 2026-09-13T17:55:15.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 161 ms · Beats 74.08%
# Memory: 40.8 MB · Beats 31.86%
# Submission: https://leetcode.com/submissions/detail/2140883563/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None : 
            return head
        
        slow, fast = head, head.next
        while fast is not None and fast.next is not None : 
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow. next = None

        left = self.sortList(head)
        right = self.sortList(right)
        return self.merge(left, right)

    def merge(self, left, right) : 
        dummy = ListNode()
        tail = dummy
        while left is not None and right is not None : 
            if left.val <= right.val : 
                tail.next = left
                left = left.next
            else : 
                tail.next = right
                right = right.next
            tail = tail.next
        
        tail.next = left if left is not None else right
        return dummy.next
