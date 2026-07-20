# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted: 2026-07-20T21:53:48.000Z
# Language: Python3
# Runtime: 51 ms · Beats 85.76%
# Memory: 29.4 MB · Beats 97.85%
# Submission: https://leetcode.com/submissions/detail/2075106524/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_area = 0
        
        while left < right : 
            current_area = (right - left) * min(height[left], height[right])
            if current_area > max_area : 
                max_area = current_area
            
            if height[left]> height[right] : 
                right -=1
            else : 
                left +=1
        
        return max_area
