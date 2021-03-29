# URL: https://leetcode.com/problems/graph-valid-tree/
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # O(N + E) runtime complexity where N is length of adjacency list
        # and E is the number of edges
        # O(N + E) space complexity for an adjacency list of length N with lengths adding up
        # to a total of E edges
        # Create adjacency list prepresentation of edges
        adjacencyList = []
        for i in range(n):
            adjacencyList.append([])
            
        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])
            
            
        # Create hashmap of parents to keep track of parents of each node
        # Check parent of each node to ensure this isn't a trivial cycle
        parent = {}
        parent[0] = -1
        stack = []
        stack.append(0)
        
        while len(stack) > 0:
            node = stack.pop(0)
            for neighbor in adjacencyList[node]:
                if parent[node] == neighbor:
                    # Trivial cycle of child -> parent
                    continue
                if neighbor in parent:
                    # Means neighbor edge is in parent so there is a cycle
                    return False
                stack.append(neighbor)
                parent[neighbor] = node
                
        return len(parent) == n
