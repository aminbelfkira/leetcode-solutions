# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# Accepted: 2026-07-21T23:08:00.000Z
# Language: Python3
# Runtime: 31 ms · Beats 35.64%
# Memory: 26 MB · Beats 66.44%
# Submission: https://leetcode.com/submissions/detail/2076418776/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        tank = 0
        n = len(gas)
        start = 0

        for i in range(n) : 
            diff = gas[i] - cost[i]
            tank +=diff
            total+=diff
            if tank <0 :
                start = i+1
                tank =0
        return start if total >= 0 else -1

