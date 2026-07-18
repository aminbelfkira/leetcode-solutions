# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted: 2026-07-18T20:25:56.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 22 ms · Beats 47.78%
# Memory: 20.2 MB · Beats 85.1%
# Submission: https://leetcode.com/submissions/detail/2072781239/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        current = 0
        max_jump = nums[0] 
        
        while current <len(nums) and current<= max_jump  : 
            max_jump = max(max_jump, current + nums[current])
            current +=1
        
        return max_jump >= len(nums) -1
