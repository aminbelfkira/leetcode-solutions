# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted: 2026-09-11T21:54:16.000Z
# Language: Python3
# Runtime: 23 ms · Beats 52.67%
# Memory: 25.7 MB · Beats 43.27%
# Submission: https://leetcode.com/submissions/detail/2138988380/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n 
        prefix =1
        for i in range(1,n) : 
            prefix *= nums[i-1]
            answer[i] = prefix

        suffix = 1
        for i in range(n-2, -1, -1) : 
            suffix *= nums[i+1]
            answer[i] *= suffix 
        
        return answer
