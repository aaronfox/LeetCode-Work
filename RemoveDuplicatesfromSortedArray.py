# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Use a two pointer approach here.
        # p1 keeps track of current index to insert element
        # p2 keeps track of unique elements
        # O(n) time complexity to iterate over all possible elements
        # O(1) space complexity as sorting in-place
        if len(nums) <= 1:
            return len(nums)
        p1 = 1
        p2 = 1
        curr_elem = nums[0]
        while p2 < len(nums):
            if nums[p2] != curr_elem:
                curr_elem = nums[p2]
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        
        return p1


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
