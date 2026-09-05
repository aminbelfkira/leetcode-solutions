# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Accepted: 2026-09-05T22:16:00.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 32.08%
# Memory: 19.2 MB · Beats 63.57%
# Submission: https://leetcode.com/submissions/detail/2132186716/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {')' : '(', '}' : '{', ']' : '['} 
        for char in s : 
            
            if char in brackets :
                print(f'{char} in brackets') 
                if len(stack) == 0 or stack.pop() != brackets[char] :
                    return False
            if char in brackets.values() :
                stack.append(char)
        return len(stack) ==0


        
