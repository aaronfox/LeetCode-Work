# URL: https://leetcode.com/problems/contains-duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Just store vals in hashmap
        # O(n) time complexity, where n represents the numbers in nums
        # O(n) space complexity
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                return True
            
        return False
