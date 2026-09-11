# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-09-11T17:59:02.000Z
# Language: Python3
# Runtime: 418 ms · Beats 98.36%
# Memory: 22.3 MB · Beats 54.52%
# Submission: https://leetcode.com/submissions/detail/2138842976/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2) : 

            target = -nums[i]
            if i >0 and nums[i] == nums[i-1] : 
                continue
            if nums[i]>0 : 
                break
            left = i+1
            right = n-1

            while left < right : 
                current_sum = nums[left]+ nums[right]
                if current_sum == target : 
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while nums[left -1] == nums[left] and left <right :
                        left +=1
                    while nums[right+1] == nums[right] and left < right :
                        right -=1
                elif current_sum >target : 
                    right -=1
                else : 
                    left +=1
        return res
