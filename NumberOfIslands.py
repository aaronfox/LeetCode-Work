# URL: https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Scan linearly through 2d grid.
        # Mark visited nodes of island as 1
        # O(m*n) runtime complexity where m and n represent the number of rows and columns
        # O(m*n) space complexity for worst case where grid map is filled with all land
        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid)
                    count += 1
        
        return count
    
    
    def dfs(self, row, col, grid):
        # Mark current element as visited
        grid[row][col] = '0'
        
        # Up, right, down, left directions
        direction_x = [-1, 0, 1, 0]
        direction_y = [0, 1, 0, -1]
        
        for i in range(len(direction_x)):
            this_row = row + direction_x[i]
            this_col = col + direction_y[i]
            
            if this_row >= 0 and this_row < len(grid) and this_col >= 0 and this_col < len(grid[0]):
                print(this_row)
                print(this_col)
                if grid[this_row][this_col] == '1':
                    self.dfs(this_row, this_col, grid)
                    
        
