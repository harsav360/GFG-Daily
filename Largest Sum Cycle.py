Given a maze with N cells. Each cell may have multiple entry points but not more than one exit(i.e entry/exit points are unidirectional doors like valves).
You are given an array Edge[] of N integers, where Edge[i] contains the cell number that can be reached from of cell i in one step. Edge[i] is -1 
if the ith cell doesn't have an exit. 
The task is to find the largest sum of a cycle in the maze(Sum of a cycle is the sum of the cell indexes of all cells present in that cycle).

Note:The cells are named with an integer value from 0 to N-1. If there is no cycle in the graph then return -1.


Kosaraju's Algorithm - 121/125 test Case passed:

from collections import defaultdict
class Solution():
    def largestSumCycle(self, N, Edge):
        #your code goes here
        def dfs(node):
            visit[node] = 1
            if node in adj:
                for ngh in adj[node]:
                    if not visit[ngh]:
                        dfs(ngh)
            stack.append(node)

        def dfs2(node):
            visit[node] = 1
            for ngh in adjT[node]:
                if not visit[ngh]:
                    dfs2(ngh)
            self.sum += node
            self.cnt1 += 1
                    
        adj = defaultdict(list)
        for i in range(N):
            if Edge[i] == -1:
                continue
            else:
                adj[i].append(Edge[i])
    
        visit = [0]*N
        stack = []
        for i in range(N):
            if not visit[i]:
                dfs(i)
        
        adjT = defaultdict(list)
        for i in range(N):
            visit[i] = 0
            for ngh in adj[i]:
                adjT[ngh].append(i)
        
        ans = 0
        self.cnt1 = 0
        cnt = 0
        self.sum = 0
        while stack:
            node = stack.pop()
            if not visit[node]:
                self.sum = 0
                cnt += 1
                self.cnt1 = 0
                dfs2(node)
            if self.cnt1 > 1:
                ans = max(ans,self.sum)
                
        if cnt == N:
            return -1
        return ans


Optimized Solution : 
  import sys
sys.setrecursionlimit(10**6)

class Solution():
    def dfs(self, graph, visited, u):
        if visited[u] == 2:
            return -1
        elif visited[u] == 1:
            res, cur = u, u
            while graph[cur] != u:
                cur = graph[cur]
                res += cur
            return res
        elif graph[u] != -1:
            visited[u] = 1
            res = self.dfs(graph, visited, graph[u])
            visited[u] = 2
            return res
        else:
            visited[u] = 2
            return -1
    
                
    def largestSumCycle(self, N, Edge):
        #your code goes here
        visited = [0]*N
        res = -1
        for u in range(N):
            res = max(res, self.dfs(Edge, visited, u))
        return res
