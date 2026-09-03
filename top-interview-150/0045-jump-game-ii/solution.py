# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-09-03T10:38:38.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.1 MB · Beats 65.89%
# Submission: https://leetcode.com/submissions/detail/2129507260/

class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = 0
        max_portee = nums[0]
        jumps = 0
        n = len(nums)
        for i in range(n-1) : 
            max_portee = max(max_portee, i+nums[i])
            if i == current_end : 
                jumps +=1
                current_end = max_portee
        
        return jumps
            
