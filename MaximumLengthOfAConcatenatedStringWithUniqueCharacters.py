# URL: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Use the power of sets!
        # Iterate through every every string in arr
        # and see if the characters in each string are unique
        # to the current possible unique set in possible_subsequence
        # by seeing if the intersection of the two sets is empty or not.
        # If the intersection is empty, append the union of that set
        # to the possible_subsequences array
        # O(s*2^N) time complexity where n is the number of strings and s is the length of the strings
        # O(s*2^N) possible space complexity as well
        
        # Include empty set
        possible_subsequences = [set()]
        
        max_length = 0
        for a in arr:
            # Ensure string doesn't have duplicate characters
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in possible_subsequences[:]:
                # If the two sets have any matching characters
                # based on the intersection of the two sets
                if a & c:
                    continue
                # Otherwise, can append new set 
                # of unique characters to possible_subsequences
                # using the union of the set
                if max_length < len(a | c):
                    max_length = len(a | c)
                    
                possible_subsequences.append(a | c)
                
        return max_length
