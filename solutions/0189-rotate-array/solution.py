# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-10-06T12:34:14.000Z
# Language: Python3
# Runtime: 34 ms · Beats 67.02%
# Memory: 35.4 MB · Beats 14.18%
# Submission: https://leetcode.com/submissions/detail/2164217112/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        nums[:] = nums[n-k:] + nums[:n-k]
        
