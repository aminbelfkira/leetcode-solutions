# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted: 2026-09-14T14:17:08.000Z
# Language: Python3
# Runtime: 63 ms · Beats 25.64%
# Memory: 29.5 MB · Beats 88.23%
# Submission: https://leetcode.com/submissions/detail/2141640138/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = 0
        while left < right :
            current_area = min(height[left], height[right]) * (right- left)
            max_area = max(max_area, current_area)

            if height[left] > height[right] : 
                right-=1
            else : 
                left +=1
        
        return max_area
