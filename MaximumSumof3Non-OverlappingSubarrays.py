# URL: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Prefix sum-like problem using three sliding windows
        # Runs in O(n) time since only use a single while loop here
        # UsesO(1) space complexity since only fixed-size lists and ints are used in place of dynamic tables and arrays
        # Keep track of best sequences
        bestSingleSeq = 0
        bestDoubleSeq = [0, k]
        bestTripleSeq = [0, k, k*2]
        
        # Each window sum
        singleSeqSum = sum(nums[0:k])
        doubleSeqSum = sum(nums[k:2*k])
        tripleSeqSum = sum(nums[2*k:3*k])
        
        # Best combined sum windows so far
        bestSingleSeqSum = singleSeqSum
        bestDoubleSeqSum = singleSeqSum + doubleSeqSum
        bestTripleSeqSum = singleSeqSum + doubleSeqSum + tripleSeqSum
        
        # Pointers to sliding window positions for each sum
        singleSeqIndex = 1
        doubleSeqIndex = 1 + k
        tripleSeqIndex = 1 + 2*k
        
        while tripleSeqIndex <= len(nums) - k:
            # Current sliding windows
            singleSeqSum = singleSeqSum - nums[singleSeqIndex - 1] + nums[singleSeqIndex + k - 1]
            doubleSeqSum = doubleSeqSum - nums[doubleSeqIndex - 1] + nums[doubleSeqIndex + k - 1]
            tripleSeqSum = tripleSeqSum - nums[tripleSeqIndex - 1] + nums[tripleSeqIndex + k - 1]

            # Update best sums where necessary
            if singleSeqSum > bestSingleSeqSum:
                bestSingleSeq = singleSeqIndex
                bestSingleSeqSum = singleSeqSum
            
            if doubleSeqSum + bestSingleSeqSum > bestDoubleSeqSum:
                bestDoubleSeq = [bestSingleSeq, doubleSeqIndex]
                bestDoubleSeqSum = doubleSeqSum + bestSingleSeqSum
                
            if tripleSeqSum + bestDoubleSeqSum > bestTripleSeqSum:
                bestTripleSeq = bestDoubleSeq + [tripleSeqIndex]
                bestTripleSeqSum = tripleSeqSum + bestDoubleSeqSum
            
            singleSeqIndex = singleSeqIndex + 1
            doubleSeqIndex = doubleSeqIndex + 1
            tripleSeqIndex = tripleSeqIndex + 1
            
        return bestTripleSeq
