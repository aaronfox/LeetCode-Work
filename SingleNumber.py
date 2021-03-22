# URL: https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # Use list. If num in curr_nums, remove it. Else, append it. Return remaining number
        # O(n^2) time complexity to search if element in nums for every number
        # O(n) space complexity using a list
#         curr_nums = []
#         for num in nums:
#             if num in curr_nums:
#                 curr_nums.remove(num)
#             else:
#                 curr_nums.append(num)
                
#         return curr_nums[0]
    
        # Use hash table to avoid n^2 time from approach above
        # O(n) time complexity since indexing hash table takes O(1) time
        # O(n) space complexity
        # Could also increment count to 2 and iterate once more through hash table to find key with val 1
        hash = {}
        for num in nums:
            if num in hash:
                del hash[num]
            else:
                hash[num] = 0

        key = list(hash.keys())
        return key[0]

    
        
