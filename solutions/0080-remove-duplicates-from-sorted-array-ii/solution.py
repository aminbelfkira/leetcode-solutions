# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Accepted: 2026-09-11T22:17:51.000Z
# Language: Python3
# Runtime: 86 ms · Beats 62.02%
# Memory: 22.1 MB · Beats 64.96%
# Submission: https://leetcode.com/submissions/detail/2138995371/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 2
        n = len(nums)
        for i in range(2, n) : 
            if nums[i] != nums[k-2] : 
                nums[k] = nums[i]
                k+=1
        return k
