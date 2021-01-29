# URL: https://leetcode.com/problems/top-k-frequent-words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # O(nlog(n)) runtime complexity to sort ordered dictionary
        # O(n) space complexity to store items in hashmap
        # Simply use a hashmap to store occurrences of each word
        hashmap = {}
        
        for word in words:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1
        
        res = []
        
        # Make sure hashmap is ordered alphabetically
        ordered_hashmap = collections.OrderedDict(sorted(hashmap.items()))

        while k > 0:
            max_occ = 0
            max_word = 0
            for key, val in ordered_hashmap.items():
                if val > max_occ:
                    max_occ = val
                    max_word = key
            ordered_hashmap[max_word] = -1
            res.append(max_word)
            k -= 1
        
        return res
    
            # A priority queue would be better here
#         import heapq
#         heap = []
#         # By default, heapq is a min heap. To make it max heap, use inverted values
#         # Sort words as they must be in ascending alphabetical order in ties
#         for word in sorted(words):
#             if word not in heap:
#                 heapq.heappush(heap, (-1, word))
#             else:
#                 heapq.heappush(heap, )
                
            
        
        
