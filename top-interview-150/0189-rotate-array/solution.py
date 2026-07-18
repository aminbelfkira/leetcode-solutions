# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-07-18T20:11:05.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 26.5 MB · Beats 70.42%
# Submission: https://leetcode.com/submissions/detail/2072773210/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k = k%n
        nums[:] = nums[n-k:] + nums[:n-k]
