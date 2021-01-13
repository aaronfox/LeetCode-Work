# URL: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        # Use stack to keep track of parens
        # O(n) runtime and O(n) stack space
        stack = [] 
        stack.append(s[0])
        for i in range(1, len(s)):
            curr = s[i]
            if len(stack) == 0:
                stack.append(curr)
            elif curr == ')' and stack[len(stack) - 1] == '(':
                stack.pop()
            elif curr == '}' and stack[len(stack) - 1] == '{':
                stack.pop()
            elif curr == ']' and stack[len(stack) - 1] == '[':
                stack.pop()
            else:
                stack.append(curr)
                
        return len(stack) == 0
            
