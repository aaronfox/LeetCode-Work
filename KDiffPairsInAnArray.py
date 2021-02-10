# URL: https://leetcode.com/problems/k-diff-pairs-in-an-array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # O(n) runtime
        # O(n) space complexity for storing hashmap of numbers and their number of occurrences
        num_unique_pairs = 0
        
        # Count up nums
        # Could also use collections.Counter(nums) here
        num_occ = {}
        for num in nums:
            if num not in num_occ:
                num_occ[num] = 1
            else:
                num_occ[num] += 1
        
        for key in num_occ:
            # If current number + k is in dict, it is one pair
            # Or if k == 0 and there is more than one occurrence of that number, increment num pairs too
            if k > 0 and key + k in num_occ or k == 0 and num_occ[key] > 1:
                num_unique_pairs += 1
        
        return num_unique_pairs
