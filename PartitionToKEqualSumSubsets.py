# URL: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Backtracking Solution
        # O(k * 2^n) time complexity for inner recursion to find a proper subset for each k value
        # O(n) since recursion tree won't be called on visited elements in array
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        if len(nums) < k:
            return False
        
        visited = [False for x in range(len(nums))]
        return self.canPartition(nums, visited, 0, k, 0, sum_nums / k)
    
    
    def canPartition(self, nums, visited, start, k, curr_sum, target_sub_sum):
        if k == 1:
            return True
        if curr_sum > target_sub_sum:
            return False
        
        # If we are at target sub_sum then return recursion to outerloop
        # where we look for division of k - 1 subsets to equal target_sub_sum
        if curr_sum == target_sub_sum:
            return self.canPartition(nums, visited, 0, k - 1, 0, target_sub_sum)
        
        # Recursive case
        for i in range(start, len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            if self.canPartition(nums, visited, i + 1, k, curr_sum + nums[i], target_sub_sum):
                return True
            visited[i] = False
        
        return False
