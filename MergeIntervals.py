# URL: https://leetcode.com/problems/merge-intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort list of lists. Then set first list to newInterval and change its second end point to the greater
        # end point of the larger lists to its right until a disjount set is met (which is determined by the second number of the prior interval being less than the first number of the next interval). Then, add the new interval to the result array
        # O(nlog(n)) runtime complexity because of the sorting
        # O(n) space complexity
        # Sort integers by first character 
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []
        # Iterate through the intervals. If the end beginning of the next interval overlaps with last number of 
        newInterval = intervals[0]
        res.append(newInterval)
        for interval in intervals:
            if (interval[0] <= newInterval[1]): # The intervals overlap since the last number of the prior interval is greater than or equal to the first num of next interval
                newInterval[1] = max(newInterval[1], interval[1])
            else: # Sets are disjoint
                newInterval = interval
                res.append(newInterval)

        return res
                
