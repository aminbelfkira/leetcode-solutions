# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Accepted: 2026-07-18T22:18:53.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 114 ms · Beats 48.52%
# Memory: 56.9 MB · Beats 42.32%
# Submission: https://leetcode.com/submissions/detail/2072823973/

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx : 
            return False
        self.values.append(val)
        self.val_to_idx[val] = len(self.values) -1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx : 
            return False
        
        last_val = self.values[-1]
        index_to_swap = self.val_to_idx[val]

        self.values[index_to_swap] = last_val
        self.val_to_idx[last_val] = index_to_swap

        self.values.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:

        import random
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
