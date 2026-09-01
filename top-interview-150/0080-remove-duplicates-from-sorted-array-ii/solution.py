# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Accepted: 2026-09-01T17:57:37.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 86 ms · Beats 62.9%
# Memory: 21.8 MB · Beats 81.89%
# Submission: https://leetcode.com/submissions/detail/2127593228/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2
        if n <= 2 : 
            return n
       
        for i in range(2, n) : 
            if nums[i] !=  nums[k-2] : 
                nums[k] = nums[i]
                k+=1
        return k      
