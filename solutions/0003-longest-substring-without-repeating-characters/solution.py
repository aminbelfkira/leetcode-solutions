# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted: 2026-09-11T17:20:57.000Z
# Language: Python3
# Runtime: 178 ms · Beats 66.16%
# Memory: 19.9 MB · Beats 53.85%
# Submission: https://leetcode.com/submissions/detail/2138800835/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0 
        longest_substring = 0
        n = len(s)
        for right, char in enumerate(s) : 
            if char in seen and seen[char] >= left : 
                left = seen[char] +1
            seen[char] = right
            longest_substring = max(longest_substring, right - left +1)
        
        return longest_substring
