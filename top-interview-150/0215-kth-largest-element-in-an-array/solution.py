# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Accepted: 2026-10-01T13:18:57.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 67 ms · Beats 76.82%
# Memory: 31 MB · Beats 71.3%
# Submission: https://leetcode.com/submissions/detail/2159221404/

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        import heapq
        for num in nums :
            if len(heap) < k : 
                heapq.heappush(heap, num) 
            else : 
                heapq.heappushpop(heap, num)
        return heap[0] 
