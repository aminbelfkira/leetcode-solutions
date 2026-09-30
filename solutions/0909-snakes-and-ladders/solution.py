# 909. Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/
# Accepted: 2026-09-30T22:53:38.000Z
# Language: Python3
# Runtime: 15 ms · Beats 87.16%
# Memory: 19.3 MB · Beats 86.78%
# Submission: https://leetcode.com/submissions/detail/2158633886/

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
        queue = deque([(1, 0)])
        while queue : 
            square, moves = queue.popleft()
            if square ==n*n : 
                return moves
            for nxt in range(square +1, min(square + 6, n*n)+1 ) : 
                dest = cells[nxt] if cells[nxt] != -1 else nxt 
                if dest not in visited : 
                    visited.add(dest)
                    queue.append((dest, moves + 1))
        return -1
