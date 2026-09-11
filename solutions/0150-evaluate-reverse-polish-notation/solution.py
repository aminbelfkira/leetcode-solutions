# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Accepted: 2026-09-11T21:42:13.000Z
# Language: Python3
# Runtime: 3 ms · Beats 54.75%
# Memory: 20.5 MB · Beats 93.76%
# Submission: https://leetcode.com/submissions/detail/2138984304/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+', '-', '/','*']

        for token in tokens : 
            if token not in operators : 
                stack.append(int(token))
            else : 
                b = stack.pop()
                a = stack.pop()
                if token == "+" : 
                    stack.append(a+b)
                elif token == '-' : 
                    stack.append(a-b)
                elif token == '*' : 
                    stack.append(a*b) 
                else : 
                    stack.append(int(a/b))
        return stack.pop()
        
