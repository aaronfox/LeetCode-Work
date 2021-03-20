# URL: https://leetcode.com/problems/word-search-ii/
class Solution:
    # O(M(4*3^(L-1)) time complexity where M is the number of cells in the 
    # board and l is the length of the longest possible word
    # O(n) space complexity for storing every letter in dictionary
    # (here, n is the total number of letters in dictionary)
    
    def __init__(self):
        self.matching_words = []
        self.board = []
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create Trie structure out of dictionaries
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            # Place '#' to mark end of word and store word as value
            node['#'] = word
            
        self.board = board
        
        # Backtrack on each cell of board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Only run backtracking on possible words 
                if board[i][j] in trie:
                    self.backtracking(i, j, trie)
                    
        return self.matching_words

                    
    def backtracking(self, row, col, node):
        letter = self.board[row][col]
        curr_node = node[letter]
        
        # See if match is found
        if '#' in curr_node:
            self.matching_words.append(curr_node['#'])
            # Make sure we don't add same letter again in word exploration
            del curr_node['#']
            
        # Mark current letter before exploring to prevent same from being counted twice in word
        self.board[row][col] = '#'
        
        # Explore neighbor cells in clockwise directions (up, right, down, left)
        row_offset = [1, 0, -1, 0]
        col_offset = [0, 1, 0, -1]
        for i in range(len(row_offset)):
            new_row = row + row_offset[i]
            new_col = col + col_offset[i]
            if new_row >= 0 and new_row < len(self.board) and new_col >= 0 and new_col < len(self.board[0]):
                if self.board[new_row][new_col] in curr_node:
                    self.backtracking(new_row, new_col, curr_node)
        
        # Finished exploring. Place letter back in board
        self.board[row][col] = letter
        
        # Optimize by removing empty leaf nodes that don't need to be checked any more
        if len(curr_node) == 0:
            del node[letter]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
