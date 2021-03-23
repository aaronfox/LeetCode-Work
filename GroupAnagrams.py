# URL: https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Could sort strings and store sorted strings in dict
        # If two sorted strings match, then they are in same group
        # O(n*k*log(n)) runtime complexity for storing each string in dictionary
        # where n is the number of strings and k is th max length of the strings
        # O(n*k) space complexity for storing all strings in hashmap
        anagrams = []
        sorted_strings = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in sorted_strings:
                sorted_strings[sorted_string].append(string)
            else:
                # Add string to its own dict entry
                sorted_strings[sorted_string] = [string]
                
        # Return list of values
        return sorted_strings.values()
                
        # Could also just get the count of each letter in a list for each string
        # and if the letter counts for each string are the same, they are in the same group
        # O(n*k) runtime complexity for running through each string of max length k
        # O(n*k) space complexity for storing each string of max k letters in hashmap
        res_map = {}
        for string in strs:
            # Create empty counts
            count = [0 for x in range(26)]
            for c in string:
                # Use basic ASCII math to get index location of each letter
                count[ord(c.lower()) - 97] += 1
                
            count_representation = ""
            for i in range(26):
                count_representation += "#"
                count_representation += str(count[i])

            if count_representation in res_map:
                res_map[count_representation].append(string)
            else:
                res_map[count_representation] = [string]
                    
        return res_map.values()
        

