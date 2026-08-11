# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
# Accepted: 2026-08-11T18:26:03.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 52 ms · Beats 19.07%
# Memory: 33.7 MB · Beats 62.38%
# Submission: https://leetcode.com/submissions/detail/2103310565/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(subs) : 
            return subs == subs[::-1]
        res = []
        path = []
        def backtrack(start):
            if start == len(s) : 
                res.append(path[:])
            
            for end in range(start +1, len(s)+1) : 
                substring = s[start : end]

                if is_palindrome(substring) : 
                    path.append(substring)
                    backtrack(end)
                    path.pop()
        backtrack(0)

        return res
