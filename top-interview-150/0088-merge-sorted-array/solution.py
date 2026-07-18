# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Accepted: 2026-07-18T01:47:41.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 76.89%
# Submission: https://leetcode.com/submissions/detail/2071655773/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
                # Pointers for nums1, nums2, and the end of nums1
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy any remaining elements from nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
