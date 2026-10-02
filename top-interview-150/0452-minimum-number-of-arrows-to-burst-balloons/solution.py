# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Accepted: 2026-10-02T22:39:46.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 61 ms · Beats 88.31%
# Memory: 53.4 MB · Beats 91.47%
# Submission: https://leetcode.com/submissions/detail/2160590904/

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows
