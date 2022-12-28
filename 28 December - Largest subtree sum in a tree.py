Given a binary tree. The task is to find subtree with maximum sum in the tree and return its sum. -Hard Level Tag
              1
            /    \
          -2      3
          / \    /  \
         4   5  -6   2
Output: 7
Explanation: 
Subtree with largest sum is : 
  -2
 /  \ 
4    5
Also, entire tree sum is also 7

Approach -> We will find the sum of every sub-tree. Create a global ans variable that will keep the maximum sum, we got so far.

Time-Complexity = O(N) Because we travering the tree only once.
Space -Complexity = O(1) if we not consider the stack space.

class Solution:
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        # code here
        def dfs(node):
            if node == None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            self.ans = max(self.ans,left_sum+right_sum+node.data)
            return left_sum+right_sum+node.data
        self.ans = float('-inf')
        dfs(root)
        return self.ans
