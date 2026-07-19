# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted: 2026-07-19T01:45:08.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 464 ms · Beats 95.56%
# Memory: 22.4 MB · Beats 31.79%
# Submission: https://leetcode.com/submissions/detail/2072876910/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        results = []
        n = len(nums)

        for i in range(n-2) : 

            if nums[i]>0 : 
                break
            
            if i>0 and nums[i] == nums[i-1] : 
                continue

            left, right = i+1, n-1
            target = -nums[i]

            while left < right: 
                current_sum = nums[left] + nums[right]

                if current_sum == target :
                    results.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left -1] : 
                        left +=1
                    while left < right and nums[right] == nums[right+1] : 
                        right -=1
                
                elif current_sum < target :
                    left +=1
                else : 
                    right -=1
        
        return results
