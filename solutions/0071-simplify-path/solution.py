# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/
# Accepted: 2026-09-11T21:37:49.000Z
# Language: Python3
# Runtime: 3 ms · Beats 37.98%
# Memory: 19.3 MB · Beats 64.73%
# Submission: https://leetcode.com/submissions/detail/2138982831/

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        path = path.split('/')

        for folder in path : 
            if folder == "" : 
                continue
            elif folder == '.' : 
                continue
            elif folder == '..' : 
                if stack :
                    stack.pop()
            else : 
                stack.append(folder)
        return "/"+ "/".join(stack)
