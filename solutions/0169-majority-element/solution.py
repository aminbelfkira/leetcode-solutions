# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# Accepted: 2026-09-11T21:17:52.000Z
# Language: Python3
# Runtime: 2 ms · Beats 87.07%
# Memory: 21 MB · Beats 84.06%
# Submission: https://leetcode.com/submissions/detail/2138975707/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = nums[0]
        compteur = 1
        for num in nums[1:] : 
            if num != majority : 
                compteur -=1
            else : 
                compteur +=1
            if compteur < 0 : 
                compteur =1
                majority = num
        return majority
        
