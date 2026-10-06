# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# Accepted: 2026-10-06T13:31:04.000Z
# Language: Python3
# Runtime: 36 ms · Beats 21.47%
# Memory: 25.9 MB · Beats 69%
# Submission: https://leetcode.com/submissions/detail/2164267667/

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        tank = 0
        start = 0
        for i in range(len(gas)) : 
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank <0 : 
                tank = 0
                start = i+1
        return start if total >= 0 else -1
