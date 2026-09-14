# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Accepted: 2026-09-14T20:31:56.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 11.45%
# Submission: https://leetcode.com/submissions/detail/2141988701/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank :
            return -1
        remaining = set(bank)
        from collections import deque
        queue = deque([(startGene, 0)])
        while queue : 
            current, mutations = queue.popleft()
            if current == endGene : 
                return mutations
            for i, base in enumerate(current) : 

                for gene in "ACGT" : 
                    if gene != base : 
                        new_gene = current[:i] + gene + current[i+1:]
                        if new_gene in remaining : 
                            queue.append((new_gene,mutations +1))
                            remaining.remove(new_gene)
        return -1
