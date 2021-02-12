# URL: https://leetcode.com/problems/matchsticks-to-square
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        # This is a form of the partition problem: https://en.wikipedia.org/wiki/Partition_problem
        # O(4^n) time complexity for n sticksand there are 4 possibilities of arranging each stick
        # O(n) space complexity for recursive stack space required for the calls
        if len(nums) < 4:
            return False
        summed = sum(nums)
        if summed % 4 != 0:
            return False
        
        # Sort nums in reverse order since it will optimize the results much faster
        return self.dfs(sorted(nums, reverse=True), [0, 0, 0, 0], 0, summed / 4)
        
    def dfs(self, nums, sums, index, target):
        print(nums,sums,index,target)
        if index == len(nums):
            if sums[0] == target and sums[1] == target and sums[2] == target:
                return True
            return False
        
        for i in range(4):
            if sums[i] + nums[index] > target:
                continue
            sums[i] += nums[index]
            if self.dfs(nums, sums, index + 1, target):
                return True
            sums[i] -= nums[index]
    	
        return False
            
