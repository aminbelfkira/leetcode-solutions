# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/
# Accepted: 2026-09-05T15:19:40.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 71.38%
# Submission: https://leetcode.com/submissions/detail/2131856307/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_to_char = {}
        char_to_word = {}

        s = s.split()
        print(s)
        if len(pattern) != len(s) : 
            return False
        for i, (char, word) in enumerate(zip(pattern, s)) : 

            if char in char_to_word and char_to_word[char] != word :
                return False
            if word in word_to_char and word_to_char[word] != char : 
                return False
            char_to_word[char] = word 
            word_to_char[word] = char
        return True
