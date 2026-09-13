# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted: 2026-09-13T21:33:13.000Z
# Language: Python3
# Runtime: 47 ms · Beats 70.19%
# Memory: 36.6 MB · Beats 37.63%
# Submission: https://leetcode.com/submissions/detail/2141028917/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set : 
            if num -1 in num_set : 
                continue
            current = 1
            while num + current in num_set : 
                current +=1
            longest = max(longest, current)

        return longest    
