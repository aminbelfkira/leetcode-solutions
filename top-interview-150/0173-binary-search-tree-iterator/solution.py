# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# Accepted: 2026-09-12T13:23:21.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 88.91%
# Memory: 25.6 MB · Beats 63.02%
# Submission: https://leetcode.com/submissions/detail/2139516799/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node) : 
        while node : 
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) >0 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
