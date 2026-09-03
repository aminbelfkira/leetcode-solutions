# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# Accepted: 2026-09-03T10:55:54.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 31 ms · Beats 35.24%
# Memory: 26 MB · Beats 67.88%
# Submission: https://leetcode.com/submissions/detail/2129521687/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        reservoir = 0
        n = len(gas)
        start = 0
        for i in range(n) : 
            diff = gas[i] - cost[i]
            total += diff
            reservoir += diff
            if reservoir <0 : 
                reservoir = 0
                start = i+1
        print(reservoir)
        return start if total >=0 else -1

        
