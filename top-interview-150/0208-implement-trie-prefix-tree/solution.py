# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Accepted: 2026-09-13T15:29:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 32 ms · Beats 72.39%
# Memory: 34 MB · Beats 71.61%
# Submission: https://leetcode.com/submissions/detail/2140743257/

class TrieNode :
    def __init__(self) : 
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for char in word : 
            if char not in node.children : 
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def _find(self, text) :
        node = self.root 
        for char in text : 
            node = node.children.get(char)
            if node is None :
                return None
        return node
        
    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
