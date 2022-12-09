def numOfWays(M, N):
    # code here
    ans = 0
    mod = 1000000007
    drow = [1,2,-1,-2,-1,2,1,-2]
    dcol = [2,1,-2,-1,2,-1,-2,1]
    for i in range(N):
        for j in range(M):
            total = (N*M)%mod
            minus = 1
            for k in range(8):
                nrow = i+drow[k]
                ncol = j+dcol[k]
                if nrow >= 0 and nrow < N and ncol >= 0 and ncol < M:
                    minus += 1
            minus = minus%mod
            total -= minus
            ans += total
            ans = ans%mod
    return ans
