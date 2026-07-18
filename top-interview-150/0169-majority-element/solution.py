# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# Accepted: 2026-07-18T20:06:09.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 57.3%
# Memory: 21.1 MB · Beats 49.39%
# Submission: https://leetcode.com/submissions/detail/2072770273/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = nums[0]
        compteur = 1

        for i in range(1,len(nums)) : 

            current = nums[i]
            if current == majority : 
                compteur +=1
            else : 
                compteur -=1
            
            if compteur < 0 : 
                compteur = -compteur
                majority = current
            
        return majority
