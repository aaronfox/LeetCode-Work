# URL: https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Keep track of pointers to top, bottom, left, and right
        # Keep iterating while top <= bottom and left <= right
        # O(n) time complexity where n is the number of elements in the matrix
        #O(n) space complexity where n is the number of elements to store in output array
        output = []
        direction = 'right'
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            if direction == 'right':
                for i in range(left, right + 1):
                    output.append(matrix[top][i])
                top += 1
                direction = 'down'
            elif direction == 'down':
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])
                right -= 1
                direction = 'left'
            elif direction == 'left':
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
                direction = 'up'
            elif direction == 'up':
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
                direction = 'right'
                
        return output
