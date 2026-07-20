# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted: 2026-07-20T22:44:58.000Z
# Language: Python3
# Runtime: 3 ms · Beats 89.02%
# Memory: 20 MB · Beats 65.84%
# Submission: https://leetcode.com/submissions/detail/2075122031/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        current_end =0
        jumps = 0
        for k in range(n-1) : 

            farthest = max(farthest, k+nums[k])
            if  k ==current_end : 
                current_end = farthest
                jumps +=1
        return jumps
