Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree
over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel
preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary
  
  
  
  Input:
        1 
      /   \
     2     3  
    / \   / \ 
   4   5 6   7
      / \
     8   9
   
Output: 1 2 4 8 9 6 7 3
  
<! Try Before Watching the Solution,- Thank You >





#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        def isLeaf(node):  #This Function will check the Leaf node
            if node.left == None and node.right == None:
                return 1
            else:
                return 0
        def addLeftNode(node): #This Function will add the left nodes data
            curr = node.left
            while curr != None:
                if not isLeaf(curr):
                    ans.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        def addLeafs(node): #this Function will add the leaf nodes
            if isLeaf(node):
                ans.append(node.data)
                return
            if node.left:
                addLeafs(node.left)
            if node.right:
                addLeafs(node.right)
        def addRightNode(node):
            curr = node.right
            temp = [] #To store the data in reverse order
            
            while curr != None:
                if not isLeaf(curr):
                    temp.append(curr.data)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            n = len(temp)-1
            for i in range(n,-1,-1):
                ans.append(temp[i])
        ans = []
        if not isLeaf(root):
            ans.append(root.data)
        addLeftNode(root)
        addLeafs(root)
        addRightNode(root)
        return ans
        
        
        

