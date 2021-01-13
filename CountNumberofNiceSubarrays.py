# URL: https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding window (prefix sum) type problem
        # Use three pointers here (i, j, and effectively count)
        i = 0 # Pointer to keep track of beginning of window
        curr_count = 0 # Keep track of nice arrays inside window
        odd_count = 0 # keep track off current num of odds in window
        nice_count = 0 # total number of nice arrays from all windows
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd_count += 1
                curr_count = 0
            while odd_count == k:
                # Starting from i pointer, subtract one from odd count if odd
                odd_count -= nums[i] % 2
                i += 1
                curr_count += 1
            nice_count += curr_count
        
        return nice_count
                
        
        
