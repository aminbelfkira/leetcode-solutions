# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted: 2026-10-07T06:46:51.000Z
# Language: Python3
# Runtime: 11 ms · Beats 12.02%
# Memory: 22.3 MB · Beats 41.18%
# Submission: https://leetcode.com/submissions/detail/2165010348/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n-1
        while left <= right : 
            current_sum = numbers[left] + numbers[right]
            if current_sum == target : 
                return  [left+1, right+1]
            elif current_sum> target : 
                right -=1
            else : 
                left+=1
        
