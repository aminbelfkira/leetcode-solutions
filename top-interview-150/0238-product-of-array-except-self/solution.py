# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted: 2026-09-03T10:49:07.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 26 ms · Beats 42.72%
# Memory: 25.4 MB · Beats 80.94%
# Submission: https://leetcode.com/submissions/detail/2129516059/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        n = len(nums)
        ans = [1] * n
        for i in range(n) :
            ans[i] = prefix
            prefix *= nums[i]
        print(ans)

        suffix = 1
        for i in range(n-1, -1, -1) : 
            ans[i] *= suffix
            suffix *= nums[i]

        return ans 
