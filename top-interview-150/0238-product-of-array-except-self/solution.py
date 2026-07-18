# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted: 2026-07-18T23:08:32.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 19 ms · Beats 74.99%
# Memory: 25.6 MB · Beats 55.09%
# Submission: https://leetcode.com/submissions/detail/2072837237/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        prefix =1

        for i in range(n) : 
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1,-1) : 
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
