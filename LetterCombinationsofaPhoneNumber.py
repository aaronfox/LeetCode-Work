# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution:
    # DFS Solution
    # O(4^n) runtime complexity for DFS since there could be four digits to go over for every call
    # O(4^n) space complexity as well for each possible digit to have a recursive call in the recursive stack
    def __init__(self):
        self.numHash = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        self.output = []
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        self.DFS(digits, "", 0)
        return self.output
    
    def DFS(self, digits, curr_string, index):
        if index == len(digits):
            self.output.append(curr_string)
            return
    
        for c in self.numHash[int(digits[index])]:
            self.DFS(digits, curr_string + c, index + 1)
        
            # Backtracking solution 
            # O(3^n * 4^m) complexity where n is the number of digits of inputs mapping to three letters and m is the number of digits that map to 4 letters
            # O(3^n * 4^m) as there are 3^n * 4^m solutions to keep track of in output array
        
#         self.phoneHashMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#         self.output = []
        
#     def letterCombinations(self, digits: str) -> List[str]:
#         if len(digits) != 0:
#             self.backtrack("", digits)
#             return self.output 
#         return []
        
#     def backtrack(self, combination: str, remaining_digits: str):
#         # Base case
#         if len(remaining_digits) == 0:
#             self.output.append( combination)
#         else:
#             # Iterate over all letters which can be be represented by the number
#             digit = remaining_digits[0]
#             letters = self.phoneHashMap[digit]
#             for i in range(len(letters)):
#                 letter = self.phoneHashMap[digit][i]
#                 self.backtrack(combination + letter, remaining_digits[1:])
            
