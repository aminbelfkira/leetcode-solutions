# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Accepted: 2026-07-18T01:46:05.000Z
# Language: Python3
# Runtime: 3 ms · Beats 45.31%
# Memory: 20.5 MB · Beats 42.33%
# Submission: https://leetcode.com/submissions/detail/2071655309/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
