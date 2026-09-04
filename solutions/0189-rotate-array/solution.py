# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-09-04T12:21:07.000Z
# Language: Python3
# Runtime: 25 ms · Beats 37.1%
# Memory: 35.1 MB · Beats 20.24%
# Submission: https://leetcode.com/submissions/detail/2130677142/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k:] + nums[:n-k]  
