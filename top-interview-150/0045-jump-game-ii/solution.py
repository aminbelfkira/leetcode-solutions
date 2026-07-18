# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-07-18T20:34:19.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 70.65%
# Memory: 20.1 MB · Beats 65.87%
# Submission: https://leetcode.com/submissions/detail/2072785589/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        current_end = 0
        jumps = 0

        for k in range(n-1) : 
            farthest = max(farthest, k+nums[k])
            if k == current_end : 
                jumps +=1
                current_end = farthest
        
        return jumps
