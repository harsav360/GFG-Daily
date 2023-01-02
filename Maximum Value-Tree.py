Given a binary tree, find the largest value in each level.

from collections import deque
class Solution:
    def maximumValue(self,node):
        # code here
        que = deque()
        que.append(node)
        result = []
        while que:
            n = len(que)
            ans = -1
            for i in range(n):
                nikalo = que.popleft()
                if nikalo.data > ans:
                    ans = nikalo.data
                if nikalo.left:
                    que.append(nikalo.left)
                if nikalo.right:
                    que.append(nikalo.right)
            result.append(ans)
        return result
        
