# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-09-13T19:50:19.000Z
# Language: Python3
# Runtime: 363 ms · Beats 99.45%
# Memory: 22.2 MB · Beats 82.23%
# Submission: https://leetcode.com/submissions/detail/2140979507/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res= []
        for i in range(len(nums) -2) : 
            target = - nums[i]
            if i >0 and nums[i-1] == nums[i] : 
                continue
            if nums[i] >0 :
                break
            left = i+1
            right = len(nums)-1

            while left < right : 
                current_sum = nums[left] + nums[right]

                if current_sum == target : 
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left -1] == nums[left] : 
                        left +=1
                    while left < right and nums[right +1] == nums[right] : 
                        right -=1
                elif current_sum > target : 
                    right -=1
                else : 
                    left +=1
        return res
