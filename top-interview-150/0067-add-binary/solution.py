# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Accepted: 2026-10-01T14:24:48.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 41.37%
# Memory: 19.4 MB · Beats 52.67%
# Submission: https://leetcode.com/submissions/detail/2159279131/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1

            carry, bit = divmod(carry, 2)
            result.append(str(bit))

        return "".join(reversed(result))
