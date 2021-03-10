# URL: https://leetcode.com/discuss/interview-question/364618/

def minSteps(array):
    # Check edge cases
    if len(array) <= 1:
        return 0
    # Iterate over reversed sorted array
    array = sorted(array) # Sorting takes O(nlog(n)) time
    # Just need to keep track of number of unique numbers that occur before 
    # each number. When a unique number occurs, increment uniqueNums
    # Can simply add numSteps to number of total uniqueNums at every iteration
    # Because each number has to go X number of level steps down to reach
    # the min number
    numSteps = 0
    numUniqueLevelsAwayFromMin = 0
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            numUniqueLevelsAwayFromMin += 1
        numSteps += numUniqueLevelsAwayFromMin

    return numSteps


if __name__ == "__main__":
    print(minSteps([50]) == 0)
    print(minSteps([10, 10]) == 0)
    print(minSteps([5, 2, 1]) == 3)
    print(minSteps([4, 2, 1]) == 3)
    print(minSteps([4, 5, 5, 4, 2]) == 6)
    print(minSteps([4, 8, 16, 32]) == 6)
    print(minSteps([4, 8, 8]) == 2)
    print(minSteps([4, 4, 8, 8, 9]) == 4)
    print(minSteps([1, 2, 2, 3, 3, 4]) == 9)
    print(minSteps([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)
