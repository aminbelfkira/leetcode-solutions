# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# Accepted: 2026-08-11T18:33:36.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 3 ms · Beats 90.63%
# Memory: 20.1 MB · Beats 10.02%
# Submission: https://leetcode.com/submissions/detail/2103321093/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ### curMin and currMax

        currMin = nums[0]
        currMax = nums[0]

        res = nums[0]
        for num in nums[1:] : 
            tmp = currMax * num
            currMax = max(num, num*currMax, num* currMin )
            currMin = min(num, tmp, num * currMin)

            res = max(currMax, res)
        return res
