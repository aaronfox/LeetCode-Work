# URL: https://leetcode.com/problems/candy/
class Solution:
    # O(n) time complexity
    # O(n) space complexity
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        # Build two arrays, leftToRight and rightToLeft
        # basing their values on their neighbor's values for the respective direction
        # The maximum of each index element of each array will be the correct value required
        leftToRight = [1 for x in range(len(ratings))]
        rightToLeft = [1 for x in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                leftToRight[i] = leftToRight[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rightToLeft[i] = rightToLeft[i + 1] + 1
            
        count = 0
        for i in range(len(ratings)):
            count += max(leftToRight[i], rightToLeft[i])
        return count
