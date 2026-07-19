# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-07-19T11:50:22.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 18 ms · Beats 31.44%
# Memory: 30.5 MB · Beats 78.52%
# Submission: https://leetcode.com/submissions/detail/2073415905/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)) : 

            current_sum+= nums[right]

            while current_sum >= target : 
                min_len = min(min_len, right- left +1)
                current_sum -= nums[left]
                left +=1
        
        return min_len if min_len != float('inf') else 0
