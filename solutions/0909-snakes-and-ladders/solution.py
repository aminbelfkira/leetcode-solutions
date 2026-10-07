# 909. Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/
# Accepted: 2026-10-07T07:20:32.000Z
# Language: Python3
# Runtime: 15 ms · Beats 86.74%
# Memory: 19.4 MB · Beats 55.82%
# Submission: https://leetcode.com/submissions/detail/2165037826/

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        cells = [0]*(n*n+1)
        label = 1
        for row in range(n-1, -1, -1) : 
            cols = range(n-1, -1, -1) if (n-1-row) %2 else range(n)
            for col in cols :
                cells[label] = board[row][col]
                label +=1
        visited = {1}
        from collections import deque 

        queue = deque([(1,0)])
        while queue : 
            current, moves = queue.popleft()
            
            if current == n*n : 
                return moves
            for nxt in range(current +1, min(current+6, n*n) +1) : 
                next_move = cells[nxt] if cells[nxt] != -1 else nxt
                if next_move not in visited : 
                    visited.add(next_move)
                    queue.append((next_move, moves +1))
        return -1
            
