Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

Approach -> Make a frequency map of remainders and check if rem == 0 or rem == k//2 then frequency must be divisible by 2 otherwise freq[rem] == freq[k-rem]
class Solution:
	def canPair(self, nuns, k):
		# Code here
		mp = {}
		for i in nuns:
		    rem = i%k
		    mp[rem] = 1+mp.get(rem,0)
		
		
		for j in nuns:
		    val = j%k
		    
		    if val == 0:
		        freq = mp[val]
		        if freq%2 != 0:
		            return False
		    elif 2*val == k:
		        freq = mp[val]
		        if freq%2 != 0:
		            return False
		    else:
		        
    		    freq1 = mp[val]
    		    if k-val in mp:
    		        freq2 = mp[k-val]
    		    else:
    		        freq2 = 0
    		    if freq1 != freq2:
    		        return False
	    return True
