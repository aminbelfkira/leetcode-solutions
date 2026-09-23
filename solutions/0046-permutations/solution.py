# 46. Permutations
# https://leetcode.com/problems/permutations/
# Accepted: 2026-09-23T09:06:38.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 36.74%
# Submission: https://leetcode.com/submissions/detail/2150691698/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        current = []
        res = [] 
        def aux() :
            if len(current) == len(nums) : 
                res.append(current.copy())
                return
            for num in nums : 
                if num not in current :
                    current.append(num)
                    aux()
                    current.pop()
        aux()
        return res
