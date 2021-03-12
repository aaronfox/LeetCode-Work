# URL: https://leetcode.com/discuss/interview-question/406031/
# Write a function that, given an array A of N integers, returns the lagest integer K > 0 
# such that both values K and -K exist in array A. If there is no such integer, 
# the function should return 0.

def largestKTwoPointers(array):
    if len(array) <= 1:
        return 0

    # Two pointers approach with sorted array
    # O(nlog(n)) time complexity due to sorting
    # O(1) space complexity
    p1 = 0
    p2 = len(array) - 1
    array = sorted(array)
    while p1 < p2:
        # -10, -9, -8, -6, 1, 6
        # See if values are same K
        if array[p1] * -1 == array[p2]:
            return array[p1] * -1
        # Check if value in left is too large
        elif array[p1] * -1 > array[p2]:
            p1 += 1
        # Else, value in right must be too large
        else:
            p2 -= 1

    return 0

# Using hashMap approach, just check if a values compliment is in hashmap. 
# If it is, check if the absoluate value of the number is the max value this far
# If so, set maxVal to that number.
# O(n) time complexity
# O(n) space complexity for the hashmap
def largestKHashMap(array):
    if len(array) <= 1:
        return 0

    maxVal = 0
    hashMap = {}
    for val in array:
        if -1 * val in hashMap:
            if abs(val) > maxVal:
                maxVal = abs(val)
        else:
            hashMap[val] = 1
    return maxVal

# Test cases
if __name__ == "__main__":
    print(largestKTwoPointers([1, 2, -2, -4])) # 3
    print(largestKTwoPointers([3, 2, -2, 5, -3])) # 2
    print(largestKTwoPointers([1, 2, 3, -4])) # 0
    print(largestKTwoPointers([-1, -1])) # 0
    print(largestKHashMap([1, 2, -2, -4]))
    print(largestKHashMap([3, 2, -2, 5, -3]))
    print(largestKHashMap([1, 2, 3, -4]))
    print(largestKTwoPointers([-1, -1]))
