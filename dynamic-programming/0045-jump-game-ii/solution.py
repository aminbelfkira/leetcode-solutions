# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-08-11T15:07:39.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 5 ms · Beats 60.87%
# Memory: 20.1 MB · Beats 65.32%
# Submission: https://leetcode.com/submissions/detail/2103008975/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) 

        current_end = 0 
        max_position = nums[0]
        jumps = 0
        for i in range(n-1) : 
            max_position = max(max_position, i+ nums[i])
            if i == current_end : 
                jumps +=1
                current_end = max_position
        
        return jumps
