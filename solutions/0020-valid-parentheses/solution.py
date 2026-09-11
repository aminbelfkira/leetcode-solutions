# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Accepted: 2026-09-11T22:26:01.000Z
# Language: Python3
# Runtime: 3 ms · Beats 32.25%
# Memory: 19.2 MB · Beats 90.99%
# Submission: https://leetcode.com/submissions/detail/2138997589/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closings = {']' : '[', '}' : '{', ')' : '('}

        for char in s : 
            if char in closings : 
                if len(stack) == 0 or stack.pop() != closings[char] :
                    return False
            if char in closings.values() : 
                stack.append(char)
        return len(stack) == 0
