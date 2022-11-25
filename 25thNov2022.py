Problem Statement ->
Shreyansh has an integer N. He is really curious about the binary representation of integers. He sees that any given integer has a number of set bits.
Now he wants to find out that how many positive integers, strictly less than N, have the same number of set bits as N.

The Brute force approach for this problem is to count all the number from 1 to less than N with set bit equal to N
def count (self, N):
        # code here 
        def set_bits(number):
            res = 0
            while number:
                if number&1:
                    res += 1
                number >>= 1
            return res
        check = set_bits(N)
        ans = 0
        for i in range(1,N):
            if set_bits(i) == check:
                ans += 1
        return ans
But its time complexity is O(N*logN), N for traversing the numbers from 1 to N, and log N for calculating the set bit of each Number. This approach will give the 
TLE error. So the optimal way is to use dynamic programming.
class Solution:
    def count (self, N):
        # code here 
        dp = [[-1]*50 for _ in range(50)]
        
        def solve(spots,ones):
            if ones > spots:
                return 0
            if ones == 0 or spots == ones:
                return 1
            if dp[spots][ones] != -1:
                return dp[spots][ones]
            res = solve(spots-1,ones-1)+solve(spots-1,ones)
            dp[spots][ones] = res
            return res
        
        out = 0
        ones = 0
        bits = 0
        
        while N != 0:
            if N&1:
                out += solve(bits,ones+1)
                ones += 1
            bits += 1
            N >>= 1
        return out
