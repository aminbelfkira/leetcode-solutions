# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# Accepted: 2026-07-18T23:15:55.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 19 ms · Beats 74.68%
# Memory: 26 MB · Beats 29.69%
# Submission: https://leetcode.com/submissions/detail/2072839161/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        tank = 0
        start = 0
        n = len(gas)
        for i in range(n) : 
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank<0 : 
                start = i+1
                tank = 0
        
        return start if total >=0 else -1


