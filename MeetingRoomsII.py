# URL: https://www.lintcode.com/problem/meeting-rooms-ii
# Meeting Rooms II
# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

def getMeetingRooms(times):
    # Sort separately created start and end times arrays. Then use two pointers.
    # If start time comes first, then a meeting has started and we need another room
    # If end time comes first, that means one meeting ended so we need one less room
    # Max number of rooms at any one time is the answer
    # O(nlog(n)) time complexity for sorting
    # O(n) space complexity for storing times in separate arrays
    startTimes = [x[0] for x in times]
    endTimes = [x[1] for x in times]
    startTimes = sorted(startTimes)
    endTimes = sorted(endTimes)
    print(startTimes)
    print(endTimes)
    i = 0
    j = 0
    currRooms = 0
    rooms = 0
    while i < len(times):
        # If start time is less than current end time,
        # then other meeting still occurring and we need another room
        if startTimes[i] < endTimes[j]:
            currRooms += 1
            rooms = max(rooms, currRooms)
            i += 1
        # If start time greater than end time, then other meeting is
        # over and we can decrement number of current rooms being used
        else:
            currRooms -= 1
            j += 1

    return rooms

# This time, use min heap on time intervals sorted by start time
# If the starting time of current interval is less than current min_heap
# then push end of current interval end time to heap since we must add another room
# Else, pop the current meeting as it has ended. The end result is the length
# of the min heap since it will still contain the remaining min number of conference
# rooms needed
import heapq
def getMeetingRooms2(times):
    if not times:
        return 0
    times = sorted(times, key=lambda x: x[0])
    # Only need end times in heap
    min_heap= [times[0][1]]

    # Start from second time interval
    for i in range(1, len(times)):
        interval = times[i]
        if interval[0] < min_heap[0]:
            heapq.heappush(min_heap, interval[1])
        else:
            # Add interval end to min heap but pop top as well
            heapq.heappushpop(min_heap, interval[1])
    return len(min_heap)

intervals1 = [(0, 30), (5, 10), (15, 20)]
print(getMeetingRooms2(intervals1))
print(getMeetingRooms2(intervals1) == 2)
# Explanation:
# We need two meeting rooms
# room1: (0, 30)
# room2: (5, 10), (15, 20)

intervals2 = [(2, 7)]
print(getMeetingRooms2(intervals2))
print(getMeetingRooms2(intervals2) == 1)
# Explanation:
# Only need one meeting room
