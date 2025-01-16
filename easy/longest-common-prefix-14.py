from typing import List

class TrieNode:
    def __init__(self, char=None):
        self.children = [None] * 26
        self.char = char
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word: str) -> None:
        if word == "":
            self.root.isEnd = True
            return

        currentNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not currentNode.children[index]:
                currentNode.children[index] = TrieNode(char)
            currentNode = currentNode.children[index]
        currentNode.isEnd = True
        return

    def printTrieDetailed(self, node=None, prefix=""): # ai
        if node is None:
            node = self.root
            print("Root")
            
        for i in range(26):
            if node.children[i]:
                char = chr(i + ord('a'))
                end_marker = "*" if node.children[i].isEnd else ""
                print(f"{prefix}└─{char}{end_marker}")
                self.printTrieDetailed(node.children[i], prefix + "  ")

    def getLongestPrefix(self) -> str:
        currentNode = self.root
        longestPrefix = ""
        while currentNode.children.count(None) == 25:
            if currentNode.isEnd: # prefix length at most upto this point
                break
            for i, child in enumerate(currentNode.children): # next letter
                if child is not None:
                    currentNode = currentNode.children[i]
                    longestPrefix += currentNode.char
                    break
        return longestPrefix
            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # space: O(n*L)
        # time: O(n*L)
        # where L is max length of word in strs

        stringsTrie = Trie()
        if any(not string for string in strs):
            return ""
        for word in strs:
            stringsTrie.insertWord(word)
        stringsTrie.printTrieDetailed()
        return stringsTrie.getLongestPrefix()
