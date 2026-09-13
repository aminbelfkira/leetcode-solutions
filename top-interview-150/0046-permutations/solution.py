# 46. Permutations
# https://leetcode.com/problems/permutations/
# Accepted: 2026-09-13T16:43:02.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 87.86%
# Submission: https://leetcode.com/submissions/detail/2140808827/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        result = []
        used = set()
        def backtrack() : 
            if len(path) == len(nums) : 
                result.append(path.copy())
            for number in nums : 
                if number in used : 
                    continue
                path.append(number)
                used.add(number)
                backtrack()
                path.pop()
                used.remove(number)
        backtrack()
        return result
