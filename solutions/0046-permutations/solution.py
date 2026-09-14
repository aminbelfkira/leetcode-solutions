# 46. Permutations
# https://leetcode.com/problems/permutations/
# Accepted: 2026-09-14T21:10:16.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 87.84%
# Submission: https://leetcode.com/submissions/detail/2142005806/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def backtrack() : 
            if len(path)==len(nums) : 
                result.append(path.copy())
                return
            for num in nums : 
                if num not in path :
                    path.append(num)
                    backtrack()
                    path.pop()
        backtrack()
        return result
