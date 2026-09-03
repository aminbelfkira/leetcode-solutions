# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-09-03T21:26:41.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 422 ms · Beats 98.21%
# Memory: 22.4 MB · Beats 32.12%
# Submission: https://leetcode.com/submissions/detail/2130107211/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        results = []

        for i in range(n-2) : 
            target = - nums[i]
            left = i+1
            right = n-1
            if i>0 and nums[i] == nums[i-1] : 
                continue
            if nums[i] > 0 :
                break 

            while left < right : 
                current_sum = nums[left] + nums[right]

                if current_sum == target :
                    results.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1] : 
                        left +=1
                    while left < right and nums[right] == nums[right+1] : 
                        right -=1
                elif current_sum >target : 
                    right -=1
                else : 
                    left +=1 
        return results

