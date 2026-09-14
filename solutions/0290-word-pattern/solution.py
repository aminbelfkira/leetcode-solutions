# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/
# Accepted: 2026-09-14T13:14:01.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 30.42%
# Submission: https://leetcode.com/submissions/detail/2141581561/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word= {}
        word_to_char = {}
        s = s.split()
        if len(pattern) != len(s) : 
            return False
        for word, char in zip(pattern, s) : 

            if char in char_to_word and char_to_word[char] != word : 
                return False
            if word in word_to_char and word_to_char[word] != char : 
                return False
            char_to_word[char] = word
            word_to_char[word] = char

        return True
