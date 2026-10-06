# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Accepted: 2026-10-06T12:08:58.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 80.47%
# Submission: https://leetcode.com/submissions/detail/2164197883/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        if endGene not in bank : 
            return -1
        
        from collections import deque
        seen = set()
        queue = deque([(startGene, 0)])
        while queue : 
            current, mutations = queue.popleft()
            seen.add(current)
            if current == endGene : 
                return mutations
            for i, current_gene in enumerate(current) : 
                for new_gene in "ACGT":
                    # print(new_gene)
                    if new_gene != current_gene : 
                        new_mutation = current[:i] + new_gene + current[i+1:]
                        # print(new_mutation)
                        if new_mutation in bank and new_mutation not in seen : 
                            queue.append((new_mutation, mutations +1))
        
        return -1
