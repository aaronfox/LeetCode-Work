# URL: https://leetcode.com/problems/word-search/
class Solution:
    def __init__(self):
        # Backtracking solution: not true DFS
        # O(n*3^l) time complexity where n is number of cells in board and l is length of word to be matched
        # O(l) space complexity where l is length of word to be matched since recursion
        # stack will not be longer than the length of the word
        self.board = None
        self.rows = 0
        self.cols = 0
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, word, 0):
                    return True
        return False
    
    def dfs(self, row, col, word, index):
        # 1. Check base case
        if index >= len(word):
            return True
        
        # 2. Check boundaries
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.board[row][col] != word[index]:
            return False
        
        # 3. Iterate through potential candidates
        foundWord = False
        
        # Keep searching in all directions if needed
        # up, right, down, left
        direction_x = [-1, 0, 1, 0]
        direction_y = [0, 1, 0, -1]
        
        # Mark path as explored before 
        self.board[row][col] = '#'
        
        for i in range(len(direction_x)):
            # Make sure all calls are within range and that we haven't visited character yet
            this_row = row + direction_x[i]
            this_col = col + direction_y[i]
            foundWord = self.dfs(this_row, this_col, word, index + 1)
            if foundWord:
                break
        
        # 4. Clean up work
        self.board[row][col] = word[index]
        
        return foundWord
            
