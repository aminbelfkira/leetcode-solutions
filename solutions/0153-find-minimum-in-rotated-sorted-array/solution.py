# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted: 2026-09-18T12:28:28.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 26.89%
# Submission: https://leetcode.com/submissions/detail/2145723095/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0 
        right = len(nums) -1

        while left < right : 
            mid = (left + right) // 2
            if nums[mid] > nums[right] : 
                left = mid +1
            else : 
                right = mid
        return nums[left]
