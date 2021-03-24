# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # If last element in array < first element, then array has 
        # been rotated at least once (or len(nums) times which is effectively the same)
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]
        
        # Algorithm: use binary search-like search for its O(log(n)) complexity
        # find mid element of array
        # if mid > first element of array, then we need to look to the right of mid
        # since the inflection point of the smaller values is to the right of mid
        # if mid < first element of array, then we need to look to the left of mid
        # since the inflection point is to the left of mid
        # Stop when nums[mid] > nums[mid + 1] meaning that nums[mid + 1] is smallest
        # or stop when nums[mid - 1] > nums[mid] meaning that nums[mid] is the smallest
        # [7, 1, 2, 3, 4, 5, 6]
        # O(nlog(n)) time complexity for using binary search
        # O(1) space complexity since no extra data structures are used here
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # Correctly set left and right vals
            if nums[mid] < nums[0]:
                # then look to left of mid
                right = mid - 1
            else:
                # then look to right of mid
                left = mid + 1
        
        return -1
