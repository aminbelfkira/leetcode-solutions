# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Accepted: 2026-09-01T17:50:34.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.4 MB · Beats 79.27%
# Submission: https://leetcode.com/submissions/detail/2127582676/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k =0
        num_set = set()
        for num in nums : 
            if num not in num_set : 
                num_set.add(num)
                nums[k] = num
                k+=1
        return k   
