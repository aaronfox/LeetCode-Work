# URL: https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        # Same as hash table implementation below except only use one pass
        # O(n) in runtime complexity and O(n) space complexity 
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            dict[nums[i]] = i
        
        # Using dict storage for O(n) runtime but O(n) memory as well
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i 
        
        for i in range(len(nums)):
            if target - nums[i] in dict and i != dict[target - nums[i]]:
                return [i, dict[target - nums[i]]]
            
            
        # Brute Force solution in O(n^2) time and O(1) space complexity
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        
        return False
        
