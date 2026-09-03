# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-09-03T10:28:10.000Z
# Language: Python3
# Runtime: 30 ms · Beats 33.2%
# Memory: 35.2 MB · Beats 14.6%
# Submission: https://leetcode.com/submissions/detail/2129498243/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k :] +nums[:n-k] 
