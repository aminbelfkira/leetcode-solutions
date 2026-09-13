# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Accepted: 2026-09-13T15:33:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 33 ms · Beats 68.95%
# Memory: 31.5 MB · Beats 93.28%
# Submission: https://leetcode.com/submissions/detail/2140746677/

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root 
        for char in word : 
            node = node.setdefault(char, {})
        node["#"] = True
    
    def _find(self, text : str) : 
        node = self.root
        for char in text :
            if char not in node :
                return None
            node = node[char]
        return node
        

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and "#" in node
        

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
