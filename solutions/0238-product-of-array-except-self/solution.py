# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted: 2026-07-21T22:47:53.000Z
# Language: Python3
# Runtime: 15 ms · Beats 93.36%
# Memory: 25.3 MB · Beats 81.14%
# Submission: https://leetcode.com/submissions/detail/2076413244/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        answer = [1] * n
        for i in range(n) : 
            answer[i] = prefix 
            prefix*= nums[i]
        suffix = 1
        for i in range(n-1, -1,-1) :
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
