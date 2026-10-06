# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Accepted: 2026-10-06T12:43:46.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 58.93%
# Submission: https://leetcode.com/submissions/detail/2164224706/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        k = 0
        for i, num in enumerate(nums) : 
            if num == val : 
                continue
            nums[k] = num
            k+=1
        return k
