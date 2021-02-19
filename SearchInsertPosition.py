# URL: https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Run binary search with n + 1 space included since index could be at end
        # O(log(n)) runtime complexity
        # O(1) space complexity
        min_index = 0
        max_index = len(nums) - 1
        while min_index <= max_index:
            index = min_index + (max_index - min_index + 1) // 2
            guess = nums[index]

            if target <= guess:
                max_index = index - 1
            elif guess == target:
                return index
            else:
                min_index = index + 1
            
        return min_index
                
                
