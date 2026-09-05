# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-09-05T11:31:54.000Z
# Language: Python3
# Runtime: 16 ms · Beats 63.98%
# Memory: 30.6 MB · Beats 16.8%
# Submission: https://leetcode.com/submissions/detail/2131652745/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        min_len = float('inf')
        current_sum = 0
        for i, num in enumerate(nums): 
            current_sum += num
            while current_sum >= target : 
                min_len = min(min_len, i-left +1)
                current_sum -= nums[left]
                left +=1
                
        return min_len if min_len != float('inf') else 0
