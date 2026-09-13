# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted: 2026-09-13T19:19:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 67.22%
# Submission: https://leetcode.com/submissions/detail/2140959387/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        while left < right : 
            mid = (left + right) //2
            if nums[mid] > nums[right] : 
                left = mid +1
            else :
                right = mid
        return nums[left]
