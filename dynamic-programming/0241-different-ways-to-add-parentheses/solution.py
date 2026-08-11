# 241. Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/
# Accepted: 2026-08-11T19:59:36.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 1 ms · Beats 46.22%
# Memory: 19.4 MB · Beats 31.41%
# Submission: https://leetcode.com/submissions/detail/2103400624/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        if expression.isdigit() : 
            return [int(expression)]
        
        results = []

        for i, char in enumerate(expression) : 
            if char in "+-*" : 
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left : 
                    for r in right :
                        if char == '+' : 
                            results.append(l + r)
                        if char == '-' : 
                            results.append(l-r)
                        if char == '*' :  
                            results.append(l*r)
        return results
