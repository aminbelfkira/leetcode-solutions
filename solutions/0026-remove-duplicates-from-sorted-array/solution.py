# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Accepted: 2026-07-18T01:36:32.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.4 MB · Beats 97.1%
# Submission: https://leetcode.com/submissions/detail/2071652451/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
