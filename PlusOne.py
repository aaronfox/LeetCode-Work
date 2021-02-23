# URL: https://leetcode.com/problems/plus-one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Harder but not cheating so much
        # Keep carrying digits as needed, then break if necessary
        # O(n) runtime complexity
        # O(n) space complexity
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        
        carry = 0
        res = []
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9 or (i == 0 and digits[i] + carry != 10):
                res.insert(0, digits[i] + carry)
                carry = 0
                break
            else:
                res.insert(0, 0)
                carry = 1
        
        if carry == 1:
                res.insert(0, 1)
        else:
            return digits[0: i] + res
        
        return res
    
            # Cheap way
        # O(n) runtime complexity
        # O(n) space complexity
        string = ""
        for digit in digits:
            string += str(digit)
        res = []
        # return string
        new_int = int(string) + 1
        for num in str(new_int):
            res.append(num)
            
        return res
