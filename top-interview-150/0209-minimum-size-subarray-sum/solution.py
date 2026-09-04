# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-09-04T10:27:21.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 15 ms · Beats 86.61%
# Memory: 30.5 MB · Beats 42.23%
# Submission: https://leetcode.com/submissions/detail/2130582704/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        n = len(nums)
        min_len = float('inf')
        current_sum = 0
        for i in range(n) : 
            current_sum += nums[i]
            while current_sum >= target : 
                min_len = min(min_len, i-left +1)
                current_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0

