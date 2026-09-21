# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Accepted: 2026-09-21T10:53:30.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 41.95%
# Submission: https://leetcode.com/submissions/detail/2148554553/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        if endGene not in bank : 
            return -1

        from collections import deque
        queue = deque([(startGene, 0)])
        seen = set()
        while queue : 
            current, mutations = queue.popleft()
            seen.add(current)
            if current == endGene : 
                return mutations
            for i, base in enumerate(current) : 
                for new_gene in 'ACGT' : 
                    if new_gene != base : 
                        modified = current[:i] + new_gene + current[i+1 :]
                        if modified not in seen and modified in bank: 
                            queue.append((modified, mutations +1))
        return -1
        
