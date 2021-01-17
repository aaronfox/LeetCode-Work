# URL: https://leetcode.com/problems/count-and-say
class Solution:
    def countAndSay(self, n: int) -> str:
        # First, implement recursively:
        # Double check these complexities..
        # O(n*l) runtime since keeps calling itself n times until at goal and has for loop of dynamic size l
        # O(n) space complexity for recursion calls and storing strings
        res = self.countAndSayHelper('1', 1, n)
        return res
        
    def countAndSayHelper(self, prev_string, n, goal):
        if n == goal:
            return prev_string
        else:
            if len(prev_string) == 1:
                return self.countAndSayHelper("11", n + 1, goal)
            
            # Count up nums in curr_string
            curr_num = ""
            curr_count = 0
            sub_res = ""
            for i in range(len(prev_string)):
                if prev_string[i] == curr_num:
                    curr_count += 1
                    if i == len(prev_string) - 1:
                        sub_res += str(curr_count) + curr_num
                else:
                    if curr_count != 0:
                        sub_res += str(curr_count) + curr_num
                    
                    curr_num = prev_string[i]
                    curr_count = 1
                    if i == len(prev_string) - 1:
                        sub_res += str(curr_count) + curr_num
            
            return self.countAndSayHelper(sub_res, n + 1, goal)
                
                
