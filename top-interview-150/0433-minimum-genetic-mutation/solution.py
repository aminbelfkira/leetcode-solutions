# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Accepted: 2026-09-13T15:23:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 41.09%
# Submission: https://leetcode.com/submissions/detail/2140738167/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        remaining = set(bank)

        if endGene not in remaining:
            return -1

        remaining.discard(startGene)
        queue = deque([(startGene, 0)])

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i, current in enumerate(gene):
                for base in "ACGT":
                    if base == current:
                        continue

                    candidate = gene[:i] + base + gene[i + 1:]

                    if candidate in remaining:
                        remaining.remove(candidate)
                        queue.append((candidate, mutations + 1))

        return -1
