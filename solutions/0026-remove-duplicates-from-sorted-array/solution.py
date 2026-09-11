# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Accepted: 2026-09-11T22:12:59.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.5 MB · Beats 42.89%
# Submission: https://leetcode.com/submissions/detail/2138993975/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for num in nums :
            if num in seen : 
                continue
            else : 
                nums[k] = num
                k+=1
                seen.add(num)
        return k
        
