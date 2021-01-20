# URL: https://leetcode.com/problems/3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums to aid in logic of two pointers in this problem 
        nums.sort()
        res = []
        
        # Since nums is sorted, can iterate through values in order
        # and increment/decrement two pointers to see if target value can be made
        # O(n^2) time complexity becaususe of the while and for lops
        # O(n) space complexity to store answer
        for i in range(0, len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                lo = i + 1
                hi = len(nums) - 1
                target = -1 * nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        res.append([nums[i], nums[hi], nums[lo]])
                        # The next two while loops avoid duplicates if some nums are the same 
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while hi > lo and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        # Always increment lo and decrement hi to move on to next potential values
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1
        return res
        
        
        # Similar to a brute force approach. Times out after 80% of cases are done
        # O(n^3) runtime complexity which is why it TLEs
        # O(n) space complexity
        if len(nums) < 3:
            return None
        
        # Store each value into hashmap such that the keys are the indices and values are the numbers
        hashmap = {}
        for i in range(len(nums)):
            hashmap[i] = nums[i]
            
        candidates = []
        for index in hashmap.keys():
            target = -1 * hashmap[index]
            # Find values that sum to target so that the sum is zero
            for key, value in hashmap.items():
                # Need index of right value
                if key != index and target - value in hashmap.values():
                    # TODO: check and make sure the index of value found at target - value is not same
                    # as key (which is value's index here)
                    if ((target - value == value  or -1 * target == target - value) and list(hashmap.values()).count(target - value) < 2) or (-1 * target == value and value == target - value and list(hashmap.values()).count(value) < 3):
                        # print('inside!')
                        # print([-1 * target, target - value, value])
                        continue
                    # Before inserting, make sure set is unique
                    isUnique = True
                    for candidate in candidates:
                        if candidate == sorted([-1 * target, target - value, value]):
                            isUnique = False
                    if isUnique:
                        candidates.append(sorted([-1 * target, target - value, value]))
        
        return candidates
                    
            
#         candidates = []
#         for index in hashmap.keys():
#             # Can then perform two sum on each fixed number where two nums have to sum to -value
#             target = -1 * hashmap[index]
#             print('===========')
#             print(target)
#             # Find two values that sum to target
#             for i in range(len(nums)):
#                 if i != index and target - nums[i] in hashmap.keys():
#                     if target - nums[i] != i in hashmap.values():
#                         print(str(target - nums[i]) + ' and ' + str(nums[i]) + ' sum to target at index ' + str(i))
#                         candidates.append([-1 * target, target - nums[i], nums[i]])

        
#         return candidates
