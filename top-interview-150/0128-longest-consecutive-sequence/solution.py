# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted: 2026-07-20T23:58:21.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 43 ms · Beats 85.35%
# Memory: 36.6 MB · Beats 37.28%
# Submission: https://leetcode.com/submissions/detail/2075141934/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest =0

        for num in num_set : 
            if num -1 not in num_set :
                length = 1
                while num+length in num_set :
                    length +=1
                longest = max(length, longest)
        return longest
