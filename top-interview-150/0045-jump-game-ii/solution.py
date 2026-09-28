# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-09-28T07:11:51.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 89.35%
# Memory: 20.1 MB · Beats 67.18%
# Submission: https://leetcode.com/submissions/detail/2155697248/

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0 
        portee = 0
        current_end = 0 

        for i, num in enumerate(nums[:-1]) : 
            portee = max(portee, i + num)
            if i == current_end : 
                current_end = portee
                jumps+=1
        
        return jumps
