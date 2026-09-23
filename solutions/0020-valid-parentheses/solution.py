# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Accepted: 2026-09-23T09:09:25.000Z
# Language: Python3
# Runtime: 5 ms · Beats 3.83%
# Memory: 19.3 MB · Beats 64.5%
# Submission: https://leetcode.com/submissions/detail/2150694295/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')' : '(', ']' : '[', '}' : '{'}

        for token in s :
            if token in brackets.values() :
                stack.append(token)
            if token in brackets.keys() : 
                if not stack :
                    return False
                if stack.pop() != brackets[token] : 
                    return False
        
        return stack ==[]
