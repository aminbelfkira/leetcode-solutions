# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted: 2026-09-03T10:34:07.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 19 ms · Beats 60.32%
# Memory: 20.4 MB · Beats 45.72%
# Submission: https://leetcode.com/submissions/detail/2129503452/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        portee = 0 

        for i in range(len(nums)-1) : 
            
            if i>portee : 
                return False
            portee = max(portee, i+ nums[i])
        
        return portee >= len(nums) -1
