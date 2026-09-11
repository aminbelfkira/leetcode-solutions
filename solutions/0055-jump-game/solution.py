# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted: 2026-09-11T21:22:28.000Z
# Language: Python3
# Runtime: 23 ms · Beats 41.64%
# Memory: 20.2 MB · Beats 84.99%
# Submission: https://leetcode.com/submissions/detail/2138977472/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        portee = nums[0]
        for i, num in enumerate(nums[:-1]) : 
            if i> portee :
                return False
            portee = max(portee, i+ num)
        return portee >= n-1 
        
