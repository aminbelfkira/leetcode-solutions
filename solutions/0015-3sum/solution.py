# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-07-20T22:02:43.000Z
# Language: Python3
# Runtime: 402 ms · Beats 99.16%
# Memory: 22.2 MB · Beats 53.7%
# Submission: https://leetcode.com/submissions/detail/2075109337/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)
        n = len(nums)
        results = []

        for i in range(n-2) : 

            target = -nums[i]

            if nums[i]>0 : 
                break
            
            if i>0 and nums[i] == nums[i-1] : 
                continue
            left = i+1
            right = n-1
            while left < right : 

                current_sum =nums[left] + nums[right]
                
                if current_sum == target : 
                    results.append([nums[i],nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left -1] : 
                        left +=1
                    while left < right and nums[right] == nums[right+1] : 
                        right -=1
                elif current_sum > target : 
                    right -=1
                else :
                    left +=1
        return results
