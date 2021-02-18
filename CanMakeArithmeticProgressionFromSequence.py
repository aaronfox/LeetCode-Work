# URL: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # O(nlog(b)) time complexity to sort array
        # O(1) space complexity
        if len(arr) == 2:
            return True
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if diff != arr[i + 1] - arr[i]:
                return False
        return True
