# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Accepted: 2026-07-18T19:59:23.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 91 ms · Beats 35.73%
# Memory: 22.4 MB · Beats 24.89%
# Submission: https://leetcode.com/submissions/detail/2072766230/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2 : 
            return n
        
        i = 2
        for k in range(2,n) : 
            if nums[k] != nums[i-2] : 
                nums[i] = nums[k]
                i = i+1
        
        return i
