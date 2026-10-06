# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Accepted: 2026-10-06T12:48:04.000Z
# Language: Python3
# Runtime: 4 ms · Beats 80.37%
# Memory: 20.9 MB · Beats 96.82%
# Submission: https://leetcode.com/submissions/detail/2164228177/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        k = 2
        for i, num in enumerate(nums[2:]) : 
            if num == nums[k-2] : 
                continue
            nums[k] = num
            k+=1
        return k
