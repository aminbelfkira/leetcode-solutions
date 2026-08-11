# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Accepted: 2026-08-11T14:58:06.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 72.61%
# Submission: https://leetcode.com/submissions/detail/2102996259/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current, open_count, close_count) : 
            if len(current) == 2*n : 
                res.append(current)
                return
            if open_count <n: 
                backtrack(current +"(", open_count+1, close_count)
            if close_count <open_count: 
                backtrack(current +")", open_count, close_count+1)
        
        backtrack('', 0,0)
        return res
