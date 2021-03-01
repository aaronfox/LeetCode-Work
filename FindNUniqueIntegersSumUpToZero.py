# URL: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Can add each number and its reverse
        # Add zero for odd nms
        # O(n) runtime complexity
        # O(n) space complexity
        res = []
        if n == 1:
            res.append(0)
        elif n % 2 == 0:
            for i in range(1, int(n / 2) + 1):
                res.append(-1 * i)
                res.append(i)
        else:
            for i in range(1, int(n / 2) + 1):
                res.append(-1 * i)
                res.append(i)
            res.append(0)
            
        return res
