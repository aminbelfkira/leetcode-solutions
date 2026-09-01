# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-09-01T18:11:37.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 23 ms · Beats 34.61%
# Memory: 35.1 MB · Beats 21.99%
# Submission: https://leetcode.com/submissions/detail/2127613221/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k :] +nums[:n-k]
