# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
# Accepted: 2026-08-11T00:10:54.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 32 ms · Beats 98.9%
# Memory: 19.4 MB · Beats 19%
# Submission: https://leetcode.com/submissions/detail/2102123906/

class Solution:
    def fib(self, n: int) -> int:
        fib = [0]* (n+1)
        fib[0] = 0
        if n>=1 : 
            fib[1] = 1
        for i in range(2,n+1) : 
            fib[i]=fib[i-1] +fib[i-2] 
        return fib[n]
