# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Accepted: 2026-07-18T19:54:19.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 92 ms · Beats 30.48%
# Memory: 21.8 MB · Beats 82.14%
# Submission: https://leetcode.com/submissions/detail/2072763199/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seens = {}
        k = 0
        for num in nums : 
            
            seen = seens.get(num,0)

            if seen <= 1 : 
                nums[k] = num
                k+=1
            
            seens[num] = seen +1
        
        return k
