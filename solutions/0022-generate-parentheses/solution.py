# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Accepted: 2026-09-14T21:18:24.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 73.76%
# Submission: https://leetcode.com/submissions/detail/2142009084/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        path = []
        result = []

        def backtrack(opened, closed) : 
            if  closed == n : 
                result.append("".join(path))
                return
            if opened < n : 
                path.append("(")
                backtrack(opened+1, closed)
                path.pop()
            if closed < opened : 
                path.append(')')
                backtrack(opened, closed +1)
                path.pop()
        
        backtrack(0,0)
        return result

        
