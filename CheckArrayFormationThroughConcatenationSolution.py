# Prompt: You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
# 
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.
#
# URL: https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Map Based Approach
        # Fill in hashmap of each index of element in array
        hashmap = {}
        for i in range(len(arr)):
            hashmap[arr[i]] = i
            
        # Evaluate if each piece can fit into the array by iterating through each piece
        for i in range(len(pieces)):
            # If first element of piece isn't in arr, then return False
            if pieces[i][0] not in hashmap:
                return False
            
            # Keep track of index of piece to make sure pieces can truly fit into arr in order
            index = hashmap[pieces[i][0]]
            
            for j in range(1, len(pieces[i])):
                if pieces[i][j] not in hashmap:
                    return False
                if hashmap[pieces[i][j]] != index + 1:
                    return False
                index = index + 1
                
        
        return True
        
        # # Brute Force Approach: Get each permutation of pieces and see if they match arr
        # perms = list(itertools.permutations(pieces))
        # print(perms)
        # arrays = []
        # for perm in perms:
        #     new_array = []
        #     for array in perm:
        #         for elem in array:
        #             new_array.append(elem)
        #     arrays.append(new_array)
        # for array in arrays:
        #     if array == arr:
        #         return True
        # return False
        
        
        
        # Only works if we can take one element from beginning of each piece at a time
        # Keep track of position of elements in each piece using an array with each entry [piece, pos]
#         piece_positions = []
#         for piece in pieces:
#             piece_positions.append([piece, 0])
            
#         # piece_array, pos in piece_positions:
#         for element in arr:
#             found_elem = False
#             for i in range(len(piece_positions)):
#                 for j in range(piece_positions[i][1], len(piece_positions[i][0])):
#                     if element == piece_positions[i][0][j]:
#                         found_elem = True
#                         piece_positions[i][1] = j + 1
#                         print("piece_positions[i][1] == " + str(piece_positions[i][1]))
            
#             if found_elem == False:
#                 return False
            
#         return True
                        
        
        
        
        
        # Only works for not caring about order of pieces
        # Place contents into dict in O(n) time
#         dicti = {}
#         for array in pieces:
#             for element in array:
#                 dicti[element] = element
        
#         # Form array
#         for elem in arr:
#             if elem not in dicti:
#                 return False
        
#         return True
            