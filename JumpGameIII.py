class Solution:
    import sys
    sys.setrecursionlimit(150000)
    def canReach(self, arr: List[int], start: int) -> bool:
        # Use depth-first search to iterate over all indices until either all indices are visited or
        # a 0 is found.
        # O(n) time complexity to iterate over n elements
        # O(n) storage space for visited array and for stack recursion space
        # NOTE: could get rid of visited array here and simply set an element
        # to its negative value since non-negative elements cannot exist in arr
        # in this problem
        
        visited = [False for i in range(len(arr))]
        
        # Iterative BFS approach which uses queue for FIFO breadth-first approach
        # Use a queue with indices here
        # TLE in while loop for 50% of cases
#         queue = [start]
#         visited[start] = True
#         while len(queue) > 0:
#             curr_index = queue.pop(0)
#             curr_step = arr[curr_index]
#             if arr[curr_index] == 0:
#                 return True
#             # Append elements of queue
#             forward_index = curr_index + curr_step
#             if forward_index < len(arr) and visited[forward_index] == False:
#                 visited[forward_index] == True
#                 queue.append(forward_index)
            
#             backward_index = curr_index - curr_step
#             if backward_index >= 0 and visited[backward_index] == False:
#                 visited[backward_index] == True
#                 queue.append(backward_index)
                
#         return False        
        
        
        
        # Recursive DFS approach
        return self.recursiveDFS(arr, start, visited)
        
    def recursiveDFS(self, arr, index, visited):
        # print(index)
        if index < len(arr) and index >= 0 and visited[index] == False:
            visited[index] = True
            return arr[index] == 0 or self.recursiveDFS(arr, index - arr[index], visited) or self.recursiveDFS(arr, index + arr[index], visited) 

        return False
