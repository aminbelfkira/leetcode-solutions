# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted: 2026-07-19T01:39:09.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 67 ms · Beats 10.83%
# Memory: 29.6 MB · Beats 67.55%
# Submission: https://leetcode.com/submissions/detail/2072875277/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) -1
        max_area = 0

        while left < right :

            width = right -left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            if height[left] < height[right] : 
                left +=1
            else : 
                right -=1
            
        return max_area
