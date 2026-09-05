# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Accepted: 2026-09-05T22:31:14.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.6 MB · Beats 73.87%
# Submission: https://leetcode.com/submissions/detail/2132191386/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ['+', '-', '/', '*']
        for token in tokens : 

            if token not in operators : 
                stack.append(token)
            else : 
                if token == "+" : 
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(int(a+b))
                elif token == "-" :
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(int(a-b))
                elif token == "*" : 
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(int(a*b))
                else :
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(int(a/b))
            #print(stack)
        return int(stack.pop())

