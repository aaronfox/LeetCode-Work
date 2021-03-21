# URL: https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # For constant space complexity and O(n) time, use four single-passes
        # O(n) time complexity for four walks of length n
        # O(1) space complexity since reusing input array
        # First check if 1 is present in nums
        containsOne = False
        for i in range(len(nums)):
            if nums[i] == 1:
                containsOne = True
                break
        
        if not containsOne:
            return 1
        
        # Clean up data: replace negatives, zeros and numbers greater than length of nums
        # with 1s
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 1
                
        # Walk along array and flip sign of each element in index a for each number a
        for i in range(len(nums)):
            val = abs(nums[i])
            if val == len(nums):
                nums[0] = -1 * abs(nums[0])
            else:
                nums[val] = -1 * abs(nums[val])
                
        # Walk along array and find first positive number which will be the missing num
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        
        # Check this last in case there is more than one number larger than n
        # which would mean answer would be at an index at end of array
        if nums[0] > 0:
            return len(nums)
        
        return len(nums) + 1
    
    
        # If not worried about space complexity,
        # can just use a set and problem becomes much simpler
        # O(n) time complexity
        # O(n) space complexity for set
        numsSet = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in numsSet:
                return i
            
        return len(nums) + 1
