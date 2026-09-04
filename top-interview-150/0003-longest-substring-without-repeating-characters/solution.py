# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted: 2026-09-04T10:43:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 190 ms · Beats 51.97%
# Memory: 20 MB · Beats 22.84%
# Submission: https://leetcode.com/submissions/detail/2130596332/

class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        left = 0
        max_substring = 0
        seen = {}
        n = len(nums)
        for i in range(n): 
            if nums[i] in seen and seen[nums[i]] >= left : 
                left = seen[nums[i]] +1
            seen[nums[i]] = i
            max_substring = max(max_substring, i - left +1)
        return max_substring
