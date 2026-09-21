# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Accepted: 2026-09-21T11:03:57.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 94.63%
# Submission: https://leetcode.com/submissions/detail/2148562461/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        

        current = []
        res = []

        def aux(opened, closed) : 
            if closed == n : 
                res.append("".join(current))
                return
            if opened < n: 
                current.append("(")
                aux(opened +1, closed)
                current.pop()
            if closed <opened : 
                current.append(")")
                aux(opened, closed +1)
                current.pop()
        aux(0,0)
        return res
