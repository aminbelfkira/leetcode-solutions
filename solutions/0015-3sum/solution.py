# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-10-06T13:55:23.000Z
# Language: Python3
# Runtime: 426 ms · Beats 97.89%
# Memory: 22 MB · Beats 94.64%
# Submission: https://leetcode.com/submissions/detail/2164292335/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2) : 
            target = -nums[i]
            if nums[i] >0 : 
                break
            if i>0 and nums[i] == nums[i-1] : 
                continue
            left = i+1
            right = n-1
            while left < right : 
                current_sum = nums[left] + nums[right]
                if current_sum == target :
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -= 1
                    
                    while left < right and nums[left -1] == nums[left] :
                        left +=1
                    while left < right and nums[right +1] == nums[right] :
                        right -=1
                elif current_sum >target : 
                    right -=1
                else : 
                    left +=1

        return res
