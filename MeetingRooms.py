# URL: https://leetcode.com/problems/meeting-rooms/
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Could sort times and make sure that every previous meeting's end time is
        # less than or equal to the next meeting's start time
        # O(nlog(n)) time complexity to sort times
        # O(1) space complexity since reusing input interval list
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        
        return True
