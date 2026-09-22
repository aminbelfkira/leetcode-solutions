# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Accepted: 2026-09-22T06:36:17.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 40.1%
# Submission: https://leetcode.com/submissions/detail/2149416022/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n -1

        while j>= 0 : 
            if i>= 0 and nums1[i]> nums2[j] : 
                nums1[k] = nums1[i]
                i-=1
            else : 
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
