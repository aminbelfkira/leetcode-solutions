# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted: 2026-09-03T21:11:00.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 57 ms · Beats 60.46%
# Memory: 29.6 MB · Beats 38.37%
# Submission: https://leetcode.com/submissions/detail/2130100633/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = 0
        while left < right : 
            min_height = min(height[left], height[right])

            max_area = max(max_area, min_height * (right- left) )

            if height[left] > height[right] : 
                right -=1
            else : 
                left +=1
        
        return max_area
