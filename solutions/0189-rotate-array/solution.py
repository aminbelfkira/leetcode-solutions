# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Accepted: 2026-09-11T21:05:10.000Z
# Language: Python3
# Runtime: 43 ms · Beats 36.42%
# Memory: 35 MB · Beats 41.4%
# Submission: https://leetcode.com/submissions/detail/2138970862/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums :
            return nums
        n = len(nums)
        k = k%n

        nums[:] = nums[n-k : ] + nums[:n-k]
        return nums
