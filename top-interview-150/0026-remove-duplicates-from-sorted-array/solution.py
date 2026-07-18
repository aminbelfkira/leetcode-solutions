# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Accepted: 2026-07-18T19:47:13.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.6 MB · Beats 42.18%
# Submission: https://leetcode.com/submissions/detail/2072758799/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = set()
        k = 0
        for num in nums : 
            if num not in seen : 
                nums[k] = num
                seen.add(num)
                k+=1
        return k            
