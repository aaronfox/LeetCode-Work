# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: Solve solution in optimal time, i.e. O(log(min(x,y))) time
        # Less Optimal Solution with O(n + m) runtime and O(n + m) space complexity
        list = []
        for num in nums1:
            list.append(num)
            
        for num in nums2:
            list.append(num)
            
        list.sort()
        
        if len(list) % 2 == 0:
            return (list[math.floor(len(list) / 2) - 1] + list[math.floor(len(list) / 2)] ) / 2
        return list[math.floor(len(list) / 2)]
