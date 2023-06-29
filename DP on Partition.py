Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

# Recursion and Memoization Approach


def matrixMultiplication(self, N, arr):
        # code here
        def solve(i,j):
            if i == j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            mini = float('inf')
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j] + solve(i,k) + solve(k+1,j)
                mini = min(steps,mini)
            memo[i][j] =  mini
            return memo[i][j]
            
        memo = [[-1 for _ in range(N)] for _ in range(N)]
        return solve(1,N-1)

# Tabulation or Bottom - UP DP
dp = [[0 for j in range(N)] for i in range(N)] # Write the Base 
        
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                optns = float('inf')
                for k in range(i,j):
                    steps = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
                    optns = min(steps,optns)
                dp[i][j] = optns
        return dp[1][N-1]
