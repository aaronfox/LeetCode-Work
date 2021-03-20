# URL: https://leetcode.com/problems/find-the-celebrity
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Use deduction in a circular way to determine if a person is a possible celebrity
        # Basically, the logic here is that we can continually check if celeb candidate
        # knows the next person. If so, then the candidate must be changed to the known
        # person as the previous candidate can't be a celeb as they know someone. Continue
        # going until last possible celeb is attained
        # O(n) time ecomplexity since only using two non-nested for loops here
        # O(1) space complexity
        possible_celeb = 0
        for i in range(1, n):
            if knows(possible_celeb, i):
                possible_celeb = i
        
        # Check is celebrity candidate is indeed a celebrity
        if self.isCelebrity(possible_celeb, n):
            return possible_celeb
        return -1
        
        
        # Brute Force solution
        # O(n^2) time complexity
        # O(1) space complexity
        for i in range(n):
            if self.isCelebrity(i, n):
                return i
        return -1
    
    def isCelebrity(self, i, length):
        for j in range(length):
            if i != j:
                if knows(i, j) or not knows(j, i):
                    return False
        return True
