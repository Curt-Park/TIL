"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/

211. Add and Search Word - Data structure design
Medium

2176

100

Add to List

Share
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isTerminal = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for ch in word:
            cur.children.setdefault(ch, TrieNode())
            cur = cur.children[ch]
        cur.isTerminal = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(self.root, word)


    def _search(self, node: TrieNode, word: str) -> bool:
        if len(word) == 1:
            return word == "." and any(child.isTerminal for child in node.children.values())\
                    or word in node.children and node.children[word].isTerminal
        if word[0] == ".":
            return any(self._search(child, word[1:]) for child in node.children.values())
        return word[0] in node.children and self._search(node.children[word[0]], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
