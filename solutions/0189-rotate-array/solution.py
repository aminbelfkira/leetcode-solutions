# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-07-20T22:36:02.000Z
# Language: Python3
# Runtime: 7 ms · Beats 53.7%
# Memory: 26.7 MB · Beats 25.97%
# Submission: https://leetcode.com/submissions/detail/2075119382/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k :] +nums[:n-k]
