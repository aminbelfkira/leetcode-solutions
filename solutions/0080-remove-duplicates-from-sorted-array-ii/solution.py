# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Accepted: 2026-09-03T20:31:17.000Z
# Language: Python3
# Runtime: 71 ms · Beats 98.8%
# Memory: 21.8 MB · Beats 81.82%
# Submission: https://leetcode.com/submissions/detail/2130081466/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 2
        n = len(nums)
        for i in range(2,n) : 

            if nums[k-2] == nums[i] : 
                continue
            else : 
                nums[k] = nums[i]
                k+=1
        return k
