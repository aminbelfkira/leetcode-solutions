# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-09-04T12:29:33.000Z
# Language: Python3
# Runtime: 10 ms · Beats 24.34%
# Memory: 20 MB · Beats 65.9%
# Submission: https://leetcode.com/submissions/detail/2130683858/

class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = 0
        portee = nums[0]
        jumps = 0
        n = len(nums)
        for i in range(n-1) : 
            portee = max(portee, i+nums[i])
            if i == current_end : 
                current_end = portee
                jumps+=1
            
        return jumps
            
