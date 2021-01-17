# URL: https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use two pointers and keep shrinking widthwise from shorter height
        # Can simply subtract from the shorter height's side since 
        # a larger next area would include only the taller side with the same width
        # O(n) runtime complexity
        # O(1) space complexity
        maxArea = 0
        pointer_1 = 0
        pointer_2 = len(height) - 1
        
        for i in range(len(height)):
            shorterheight = 2
            if height[pointer_1] <= height[pointer_2]:
                shorterheight = 1
            
            if shorterheight == 1:
                area = height[pointer_1] * (pointer_2 - pointer_1)
                pointer_1 += 1
            else:
                area = height[pointer_2] * (pointer_2 - pointer_1)
                pointer_2 -= 1

            if area > maxArea:
                maxArea = area
                
            if pointer_1 == pointer_2:
                break
        
        return maxArea

            
            
