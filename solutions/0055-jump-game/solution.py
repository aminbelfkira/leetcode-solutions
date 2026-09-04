# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted: 2026-09-04T12:23:08.000Z
# Language: Python3
# Runtime: 18 ms · Beats 63.38%
# Memory: 20.2 MB · Beats 62.56%
# Submission: https://leetcode.com/submissions/detail/2130678753/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        portee = nums[0]
        n = len(nums)
        for i in range(1,n) : 
            if i> portee : 
                return False
            portee = max(portee, i+ nums[i])
        return portee >=(n-1)    
