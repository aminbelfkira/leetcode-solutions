# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/
# Accepted: 2026-07-20T23:17:59.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 68.88%
# Submission: https://leetcode.com/submissions/detail/2075130909/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words) : 
            return False
        
        n = len(pattern) 
        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words) : 
            if c in char_to_word and char_to_word[c] != w : 
                return False

            if w in word_to_char and word_to_char[w] != c :
                return False

            word_to_char[w] = c 
            char_to_word[c] = w 

        return True  

            
