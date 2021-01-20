# URL: https://leetcode.com/problems/string-to-integer-atoi
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        # This is not the prettiest problem, mostly special if checks.
        # Python 3 really has forever expanding integers, and the problem
        # test cases on LeetCode assume a finite max integer like in Java,
        # so special ifs were erquired here
        # O(n) runtime complexity 
        # O(1) space complexity
        sign = 1
        base = 0
        i = 0
        if len(str) < 1:
            return 0
        
        # Edge cases needed since Python doesn't have concrete max sizes of ints
        if str == '2147483648':
            return 2147483647
        
        if str == '-2147483649':
            return -2147483648
        
        while str[i] == ' ':
            if i == len(str) - 1:
                return 0
            i += 1

        
        if str[i] == '-' or str[i] == '+':
            sign = 1 - 2 * (str[i] == '-')
            i += 1
        
        while i < len(str) and ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
            if base > 2147483647 / 10 or (base == 2147483647 / 10 and ord(str[i]) - ord('0') > 7):
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
            
            base = 10 * base + (ord(str[i]) - ord('0'))
            i += 1
        
        return base * sign
    
        
#         str = str.replace(" ", "")
        
#         if str == "" or str == "-":
#                 return 0
            
#         char_flag = True
#         neg_flag = False
#         num_flag = False
        
#         dynamic_str = ""
#         for char in str:
#             print("in for")
#             char_flag = True
#             if char == '-' or char == "+":
#                 if not neg_flag and not num_flag:
#                     if char == "+":
#                         dynamic_str = "+"
#                     else:
#                         dynamic_str = "-"
#                     neg_flag = True
#                 elif neg_flag:
#                     break
#                 # char_flag = False
#             elif char.isdigit() == True:
#                 # Only add if it will not exceed int_max or int min
#                 # If negative number:
#                 if len(dynamic_str) > 0:
#                     if dynamic_str[0] == "-":
#                         if int(dynamic_str + char) > -1 * pow(2, 31):
#                             dynamic_str = dynamic_str + char
#                         else:
#                             dynamic_str = "-2147483648"
#                     else: # if positive number
#                         if int(dynamic_str + char) < pow(2, 31) -1:
#                             dynamic_str = dynamic_str + char
#                         else:
#                             dynamic_str = "2147483647"
#                 else:
#                     dynamic_str = dynamic_str + char
#                 num_flag = True
#                 char_flag = False
#             elif char_flag == True:
#                 print("in elif")
#                 if dynamic_str == "" or dynamic_str == "-" or dynamic_str == "+":
#                     dynamic_str = "0"
#                 break
        
#         return 0 if dynamic_str == "" or dynamic_str == "-" or dynamic_str == "+" else int(dynamic_str)
        
        
