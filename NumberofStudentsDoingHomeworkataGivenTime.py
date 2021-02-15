# URL: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # This one's really straightforward.
        # Just have one for loop and check if the start time
        # is less than the queryTime and if the end time is greater than the query time
        # O(n) runtime complexity
        # O(1) space complexity
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                res += 1
        return res
