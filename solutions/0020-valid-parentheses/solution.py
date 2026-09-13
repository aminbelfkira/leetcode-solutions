# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Accepted: 2026-09-13T21:38:32.000Z
# Language: Python3
# Runtime: 3 ms · Beats 32.4%
# Memory: 19.4 MB · Beats 5.25%
# Submission: https://leetcode.com/submissions/detail/2141030859/

class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {']': '[', ')' : '(', '}' : '{'}

        stack = []

        for token in s : 
            if token in brackets : 
                if not stack : 
                    return False
                if stack.pop() != brackets[token] : 
                    return False
            if token in brackets.values() : 
                stack.append(token)
        return len(stack) == 0
