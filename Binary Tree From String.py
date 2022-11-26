Construct a binary tree from a string consisting of parenthesis and integers. The whole input represents a binary tree.
It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the roots value and a pair of parenthesis contains a child binary tree
with the same structure. Always start to construct the left child node of the parent first if it exists.

Input: "4(2(3)(1))(6(5))"
Output: 3 2 1 4 5 6
Explanation:
           4
         /   \
        2     6
       / \   / 
      3   1 5
      
class Solution:
    def treeFromString(self, s : str) -> Optional['Node']:
        # code here
        def _solve(i):
            vs = []
            while i<N and '0'<=s[i]<='9':
                vs.append(s[i])
                i+=1
            nd = Node( int(''.join(vs) ) )
            if i<N and s[i]=='(': 
                nd.left,  i = _solve(i+1)
            if i<N and s[i]=='(': 
                nd.right, i = _solve(i+1)
            return nd, i+1 
    
        N = len(s)
        root, _ = _solve(0)
        return root
