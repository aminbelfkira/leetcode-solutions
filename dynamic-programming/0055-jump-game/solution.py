# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted: 2026-08-11T15:14:09.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 10 ms · Beats 93%
# Memory: 20.4 MB · Beats 46.01%
# Submission: https://leetcode.com/submissions/detail/2103017529/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        portee = 0
        for i in range(len(nums)-1) : 

            if i> portee : 
                return False
            portee = max(portee, i+nums[i])
        
        return portee >= len(nums) -1
