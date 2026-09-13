# 427. Construct Quad Tree
# https://leetcode.com/problems/construct-quad-tree/
# Accepted: 2026-09-13T18:18:56.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 107 ms · Beats 9.29%
# Memory: 20.2 MB · Beats 60.88%
# Submission: https://leetcode.com/submissions/detail/2140908834/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(row, col, size) :
            if size == 1 : 
                return Node(bool(grid[row][col]), True)
            
            half = size//2
            children = [build(row, col, half), build(row, col + half, half), build(row+ half, col, half), build(row+half, col+ half, half)]

            value = children[0].val
            if all(child.isLeaf and child.val == value for child in children) :
                return Node(value, True)
            
            return Node(False, False, *children)
        return build(0,0, len(grid))
        
