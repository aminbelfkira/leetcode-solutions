# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Accepted: 2026-09-05T11:17:30.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19 MB · Beats 98.38%
# Submission: https://leetcode.com/submissions/detail/2131641183/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        for num in nums :
            if num == val : 
                continue
            else : 
                nums[k] = num
                k+=1
        return k
