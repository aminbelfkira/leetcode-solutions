# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Accepted: 2026-07-18T19:44:33.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 88.12%
# Submission: https://leetcode.com/submissions/detail/2072757076/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        for num in nums : 
            if num != val : 
                nums[k] = num
                k+=1
        return k
