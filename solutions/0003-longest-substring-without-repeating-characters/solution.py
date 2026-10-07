# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted: 2026-10-07T06:37:52.000Z
# Language: Python3
# Runtime: 175 ms · Beats 90.27%
# Memory: 20 MB · Beats 37.05%
# Submission: https://leetcode.com/submissions/detail/2165002278/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = {}
        left = 0 
        for right, char in enumerate(s) : 
            if char in seen and seen[char] >= left : 
                left = seen[char] +1
            seen[char] = right
            max_len = max(max_len, right - left +1)
        return max_len
