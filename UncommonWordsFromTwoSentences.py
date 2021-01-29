# URL: https://leetcode.com/problems/uncommon-words-from-two-sentences
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # Just build a simple hashmap that keeps track of how many of each word have occurred
        # If a word only occurred once from both sentences, append it to result
        # O(n + m + p) runtime complexity where n is the number of unique words, n the length of words_a
        # and p the length of words_b
        # O(n) space complexity where n is the number of unique words in the two strings
        word_hashmap = {}
        words_a = A.split(" ")
        words_b = B.split(" ")

        for word in words_a:
            if word in word_hashmap:
                word_hashmap[word] += 1
            else:
                word_hashmap[word] = 1
                
        for word in words_b:
            if word in word_hashmap:
                word_hashmap[word] += 1
            else:
                word_hashmap[word] = 1
                
        res = []
        for key, val in word_hashmap.items():
            if val == 1:
                res.append(key)
                
        return res
