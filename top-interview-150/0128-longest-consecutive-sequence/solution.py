# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted: 2026-09-05T21:38:21.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 47 ms · Beats 70.6%
# Memory: 36.5 MB · Beats 86.84%
# Submission: https://leetcode.com/submissions/detail/2132173968/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set : 
            if num -1 in num_set :
                continue
            current = 1
            while num +current in num_set :
                current +=1
            longest = max(longest, current)
        return longest

