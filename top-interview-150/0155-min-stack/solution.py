# 155. Min Stack
# https://leetcode.com/problems/min-stack/
# Accepted: 2026-10-02T22:37:37.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 120 ms · Beats 17.62%
# Memory: 31.1 MB · Beats 73.32%
# Submission: https://leetcode.com/submissions/detail/2160590360/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
