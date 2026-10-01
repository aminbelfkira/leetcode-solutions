# 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Accepted: 2026-10-01T14:15:44.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 76 ms · Beats 83.68%
# Memory: 39.4 MB · Beats 64.35%
# Submission: https://leetcode.com/submissions/detail/2159271084/

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        import heapq
        if not nums1 or not nums2 or k <= 0 : 
            return []
        
        heap = [(nums1[i]+ nums2[0], i , 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)

        result = []
        while heap and len(result) < k : 
            _,i,j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j+1 < len(nums2) :
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return result
