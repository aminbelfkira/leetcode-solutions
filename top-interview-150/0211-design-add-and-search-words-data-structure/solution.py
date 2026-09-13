# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Accepted: 2026-09-13T16:26:16.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 1060 ms · Beats 33%
# Memory: 68.5 MB · Beats 43.83%
# Submission: https://leetcode.com/submissions/detail/2140792805/

class TrieNode : 
    def __init__(self) :     
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root 
        for char in word : 
            if char not in node.children : 
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(node, index) : 
            if index == len(word) : 
                return node.is_word 
            char = word[index]
            if char == "." :
                return any(dfs(child, index + 1) for child in node.children.values())
            child = node.children.get(char)
            return child is not None and dfs(child, index +1)
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
