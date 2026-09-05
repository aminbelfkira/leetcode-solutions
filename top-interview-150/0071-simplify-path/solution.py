# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/
# Accepted: 2026-09-05T22:20:46.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19 MB · Beats 98.83%
# Submission: https://leetcode.com/submissions/detail/2132188269/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        res = []
        for folder in path : 
            if folder == "" : 
                continue
            elif folder ==".." :
                if stack : 
                    stack.pop()
            elif folder == '.' : 
                continue
            else : 
                stack.append(folder)
        return "/" + "/".join(stack)
