# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Accepted: 2026-09-13T15:24:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 78.78%
# Submission: https://leetcode.com/submissions/detail/2140739025/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        if startGene == endGene : 
            return 0
        
        remaining = set(bank)
        if endGene not in remaining :
            return -1
        remaining.discard(startGene)
        queue = deque([(startGene, 0)])
        while queue : 
            gene , mutation = queue.popleft()
            if gene == endGene : 
                return mutation
            
            for i, current in enumerate(gene) : 
                for base in "ACGT" : 
                    if base == current :
                        continue
                    candidate = gene[:i] +base + gene[i+1 :]
                    if candidate in remaining : 
                        remaining.remove(candidate)
                        queue.append((candidate, mutation +1))
        return -1
