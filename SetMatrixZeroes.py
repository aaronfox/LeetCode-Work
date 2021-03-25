# URL: https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Place flag marker 0 to indicate if a row or col will be zeroed out
        # isCol represents if first column is 0 or not
        # O(n*m) runtime complexity
        # O(1) space complexity
        isCol = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                isCol = True
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
                    
        for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
       
        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if isCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
#         for row in range(len(matrix)):
            
#         # O(n*m) time complexity
#         # O(n + m) space complexity where n is rows and m is cols
#         # Go row by row, checking if 0 is in solution
#         zeroRows = []
#         zeroCols = []
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 if matrix[row][col] == 0:
#                     zeroRows.append(row)
#                     zeroCols.append(col)
        
#         for row in zeroRows:
#             for j in range(len(matrix[0])):
#                 matrix[row][j] = 0
                
#         for col in zeroCols:
#             for j in range(len(matrix)):
#                 matrix[j][col] = 0

                
        
        
