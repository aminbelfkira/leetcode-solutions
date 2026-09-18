# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-09-18T12:49:47.000Z
# Language: Python3
# Runtime: 367 ms · Beats 99.44%
# Memory: 22.4 MB · Beats 32.92%
# Submission: https://leetcode.com/submissions/detail/2145738128/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n -2) : 

            target = -nums[i]
            if i> 0 and nums[i] == nums[i-1] :
                continue
            if nums[i] >0 : 
                break
            left = i +1
            right = n-1

            while left < right : 
                current_sum = nums[left] + nums[right]
                if current_sum == target : 
                    res.append([nums[i],nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1] : 
                        left +=1
                    while left < right and nums[right] == nums[right +1] :
                        right -=1
                elif current_sum < target : 
                    left +=1
                else :
                    right -=1
        return res
