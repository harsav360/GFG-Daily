Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.


def isSubsetSum (self, N, arr, total):
        # code here
        #Remove memo part to make this solution complete Recursive ; TC -> O(2^n), for memo = O(N*target)
        def solve(index,target):
            if target == 0:
                return True
            if index == 0:
                return arr[index] == target
            if memo[index][target] != -1:
                return memo[index][target]
            notTake = solve(index-1,target)
            take = False
            if target >= arr[index]:
                take = solve(index-1,target-arr[index])
            memo[index][target] = notTake or take
            return notTake or take
        memo = [[-1 for j in range(total+1)] for i in range(N)]
        return solve(N-1,total)
