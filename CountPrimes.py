# URL: https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        # Use Sieve of Eratosthenes 
        # O(nlog(log(n))) time complexity
        # O(n) space complexity
        if n < 3:
            return 0
        isPrime = [True for x in range(n)]
        isPrime[0] = False
        isPrime[1] = False
        # Sieve
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
                
        # Count up primes left
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        
        return count
