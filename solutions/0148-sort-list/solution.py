# 148. Sort List
# https://leetcode.com/problems/sort-list/
# Accepted: 2026-10-01T07:45:33.000Z
# Language: Python3
# Runtime: 163 ms · Beats 74.75%
# Memory: 40.5 MB · Beats 87.67%
# Submission: https://leetcode.com/submissions/detail/2158973268/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        
        if head is None or head.next is None : 
            return head
        slow, fast = head, head.next
        while fast is not None and fast.next is not None : 
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
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
