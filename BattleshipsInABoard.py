# URL: https://leetcode.com/problems/battleships-in-a-board/
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # O(n*m) runtime complexity where n and m represent number of rows and cols respectively
        # O(1) sppace complexity
        # Can count cells that do not have an x above or to left
        rows = len(board)
        cols = len(board[0])
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '.':
                    continue
                if row > 0 and board[row - 1][col] == 'X':
                    continue
                if col > 0 and board[row][col - 1] == 'X':
                    continue
                count += 1
                
        return count
