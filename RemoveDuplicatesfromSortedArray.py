# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Keep iterating up the list and, every time the next number is not equal to 
        # its predecessor, add that unique value to current index starting at 1 and then increment index
        # O(n) runtime complexity
        # O(1) space complexity
        if len(nums) < 2:
            return len(nums)
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return index
