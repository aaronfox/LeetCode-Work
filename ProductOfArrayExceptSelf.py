# URL: https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Since we must avoid division, take advantage of the fact
        # that product of all numbers to left of index times
        # all numbers to right of index is equal
        # to the product of all numbers except the number at that index
        # O(n) time complexity since all for loops or sequential and not nested
        # O(n) space complexity for storing arrays
        # Top help reduce space complexity such that only the
        # return array is used, we could just have left array
        # and a single int variable R that multiplies by itself in a reversed
        # for loop to keep track of product of numbers on right side
        # and then multiplying that R by each value in left array
        # and then returning left array
        left = [0 for x in range(len(nums))]
        right = [0 for x in range(len(nums))]
        
        # Fill in product of all numbers left of index
        # Product of no nums is 0 for base case
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i - 1]

        # Fill in product of all numbers to right of index
        right[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(left)
        print(right)

        # # Then multiply left * right for each index in output array
        # answer = [0 for x in range(len(nums))]
        # for i in range(len(nums)):
        #     answer[i] = left[i] * right[i]
        # return answer           
    
        # Can avoid creating answer array to save space complexity
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left
