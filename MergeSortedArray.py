# URL: https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Save on space complexity by going from right end to beginning instead
        # and not creating copy of nums1
        # O(n+m) runtime complexity
        # O(1) space complexity since reusing input arrays and no extra structures are created
        # This method works becayse the pointer i can only be decremented by n steps,
        # meaning that even if all the numbers in nums2 are larger than all numbers in nums1
        # no original numbers of nums1 will be overwritten
        if len(nums1) < 1 and len(nums2) < 1:
            return
        if len(nums1) < 1:
            return nums2
        if len(nums2) < 1:
            return nums1
        
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        
        while i > -1:
            if p2 < 0 or p1 > -1 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        
        return nums1
        
        
        # Merge into nums1 after making a copy of nums1
        # O(n+m) runtime complexity to iterate over all nums
        # O(n) space complexity to store copy of nums1
        if len(nums1) < 1 and len(nums2) < 1:
            return
        if len(nums1) < 1:
            return nums2
        if len(nums2) < 1:
            return nums1

        # Create copy of nums1
        nums1_copy = []
        for i in range(m):
            nums1_copy.append(nums1[i])
            
        # Pointer to list 1
        p1 = 0
        # Pointer to list 2
        p2 = 0
        
        i = 0
        while i < len(nums1):
            if p2 >= n or p1 < m and nums1_copy[p1] < nums2[p2]:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
            i += 1
        return nums1
