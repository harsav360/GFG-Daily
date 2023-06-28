Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing.

def LongestBitonicSequence(self, nums):
		# Code here
		
		# First will calculate the LIS
		n = len(nums)
		dp1 = [1 for i in range(n)]
		for ind in range(n):
		    for prev in range(ind):
		        if nums[ind] > nums[prev] and 1+dp1[prev] > dp1[ind]:
		            dp1[ind] = 1 + dp1[prev]
		# Second, we will calculate LDS
		dp2 = [1 for _ in range(n)]
		nums.reverse()
		for ind in range(n):
		    for prev in range(ind):
		        if nums[ind] > nums[prev] and 1+dp2[prev] > dp2[ind]:
		            dp2[ind] = 1 + dp2[prev]
		dp2.reverse()
		ans = 1
		for i in range(n):
		    ans = max(ans,dp1[i]+dp2[i]-1)
		return ans
