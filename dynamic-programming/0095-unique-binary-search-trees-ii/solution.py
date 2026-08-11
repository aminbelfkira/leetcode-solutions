# 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Accepted: 2026-08-11T16:25:42.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 3 ms · Beats 55.57%
# Memory: 20.5 MB · Beats 26.67%
# Submission: https://leetcode.com/submissions/detail/2103118164/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(low, high) :
            if low > high :
                return [None]
            
            trees= []
            for i in range(low, high+1) : 
                left_subtrees = build(low, i-1)
                right_subtrees = build(i+1, high)
                for left in left_subtrees : 
                    for right in right_subtrees : 
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        return build(1, n) if n>0 else []







        # def build(low, high):
        #     if low > high:
        #         return [None]  # sous-arbre vide, mais on veut quand même une itération
            
        #     trees = []
        #     for i in range(low, high + 1):
        #         left_subtrees = build(low, i - 1)
        #         right_subtrees = build(i + 1, high)
                
        #         for left in left_subtrees:
        #             for right in right_subtrees:
        #                 root = TreeNode(i)
        #                 root.left = left
        #                 root.right = right
        #                 trees.append(root)
        #     return trees

        # return build(1, n) if n > 0 else []
