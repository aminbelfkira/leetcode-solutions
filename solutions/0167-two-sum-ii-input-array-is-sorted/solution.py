# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted: 2026-09-11T21:52:00.000Z
# Language: Python3
# Runtime: 2 ms · Beats 83.89%
# Memory: 22.4 MB · Beats 9.25%
# Submission: https://leetcode.com/submissions/detail/2138987644/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        counter = {}

        for i, num in enumerate(numbers) : 
            if num in counter : 
                return [counter[num]+1, i+1]
            counter[target - num] = i
        
        
