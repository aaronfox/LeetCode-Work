# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n) time complexity to visit each node once using preorder DFS traversal for both 
# serialize and deserialize functions
# O(n) space complexity for recursive stack calls for every node
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                res.append('None')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        res = []

        dfs(root)
        
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def recursiveDeserialize(stringList):
            if stringList[0] == 'None':
                stringList.pop(0)
                return None
            
            root = TreeNode(stringList[0])
            stringList.pop(0)
            root.left = recursiveDeserialize(stringList)
            root.right = recursiveDeserialize(stringList)
            
            return root
        
        return recursiveDeserialize(data.split(','))
            
        # NOTE: this is Level order BFS so doesn't work
        # since we serialized data using preorder traversal
#         # Avoid recursion here by using a queue for practice
#         if not data:
#             return None
#         data = data.split(",")
#         root = TreeNode(int(data[0]))
#         queue = []
#         queue.append(root)
#         i = 1
#         while len(queue) > 0 and i < len(data):
#             node = queue.pop(0)
#             if data[i] != 'None':
#                 left = TreeNode(int(data[i]))
#                 node.left = left
#                 queue.append(left)
#             i += 1
#             if data[i] != 'None':
#                 right = TreeNode(int(data[i]))
#                 node.right = right
#                 queue.append(right)
#             i += 1
        
#         return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
