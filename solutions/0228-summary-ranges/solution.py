# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/
# Accepted: 2026-09-11T21:29:18.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 25.97%
# Submission: https://leetcode.com/submissions/detail/2138979975/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        k = 0
        n = len(nums)
        result = []
        while k < n : 

            start = k
            while k+1 < n and nums[k+1] == nums[k] +1 :
                k+=1
            if start == k : 
                result.append(str(nums[k]))
            else : 
                result.append(f"{nums[start]}->{nums[k]}")
            k+=1
        return result
