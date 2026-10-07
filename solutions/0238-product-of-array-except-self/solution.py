# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted: 2026-10-07T06:43:26.000Z
# Language: Python3
# Runtime: 23 ms · Beats 53.07%
# Memory: 25.6 MB · Beats 53.86%
# Submission: https://leetcode.com/submissions/detail/2165007368/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix =1
        n = len(nums)
        answer = [1] * n 
        for i in range(n) :
            answer[i] = prefix
            prefix *= nums[i]
        print(answer)
        suffix = 1
        for i in range(n-1, -1, -1) : 
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
