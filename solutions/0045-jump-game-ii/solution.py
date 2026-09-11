# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-09-11T16:38:43.000Z
# Language: Python3
# Runtime: 7 ms · Beats 51.48%
# Memory: 20.3 MB · Beats 15.88%
# Submission: https://leetcode.com/submissions/detail/2138754822/

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        current_end = 0
        portee = nums[0]
        jumps = 0
        n = len(nums)

        for i in range(n-1) : 
            portee = max(portee, i + nums[i])
            if i == current_end : 
                jumps+=1
                current_end = portee
        return jumps
