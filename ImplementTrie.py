# URL: https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.links = {} # fill with other Trie

        # Use # to indicate end of word
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.links
        for i in range(len(word)):
            currChar = word[i]
            if currChar not in node:
                node[currChar] = {}
            node = node[currChar]
        node['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.links
        for c in word:
            if c not in node:
                return False
            node = node[c]
        # If at end after for loop, this is a word
        if '#' in node:
            return True
        # Else we are still in the middle of a word even though the letters matched up so far
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.links
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
