# URL: https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One pass solution using three pointers
        # p0 points to rightmost boundary of zeros
        # p2 points to leftmost boundary of 2s
        # curr points to index of current element (curr >= p0)
        # Keep moving curr along array. if nums[curr] = 0 then swap with nums[p0]
        # if nums[curr = 2, then swap with nums[p2]
        # This is a variant of quicksort known as three-way quicksort partitioning
        # O(n) time complexity as it's a one pass solution
        # O(1) space complexity since this is sorting in place
        p0 = 0
        p2 = len(nums) - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                # Can increment both p0 and curr here
                # Since we know that the element at p0 was
                # either 0 or 1 and not 2 since we would have
                # swapped the two with p2 already
                nums[curr] = nums[p0]
                nums[p0] = 0
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                # Don't increment curr here since we haven't sorted the element
                # found at p2 yet
                nums[curr] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            elif nums[curr] == 1:
                # Can increment curr here since we kno
                curr += 1
                
