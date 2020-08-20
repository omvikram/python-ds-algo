# This method is basically an extension to the recursive approach so that we can overcome the problem of 
# calculating redundant cases and thus increased complexity. Ce can solve this problem by simply creating a 2-D array
#  that can store a particular state (n, w) if we get it the first time. Now if we come across the same state (n, w) 
#  again instead of calculating it in exponential complexity we can directly return its result stored in the table 
#  in constant time. 

# This is the memoization approach of 
# 0 / 1 Knapsack in Python in simple 
# we can say recursion + memoization = DP 

# Ce initialize the matrix with -1 at first. 
t = [[-1 for i in range(C + 1)] for j in range(n + 1)] 

def knapsack(wt, val, C, n):	 

	# base conditions 
	if n == 0 or C == 0: 
		return 0
	if t[n][C] != -1: 
		return t[n][C] 

	# choice diagram code 
	if wt[n-1] <= C: 
		t[n][C] = max(val[n-1] + knapsack(wt, val, C-wt[n-1], n-1), knapsack(wt, val, C, n-1)) 
		return t[n][C] 
	elif wt[n-1] > C: 
		t[n][C] = knapsack(wt, val, C, n-1) 
		return t[n][C] 

# driver code 
val = [60, 100, 120] 
wt = [10, 20, 30] 
C = 50
n = len(val) 

print(knapsack(wt, val, C, n)) 

# Time Complexity: O(N*W)
# where ‘N’ is the number of weight element and ‘W’ is capacity.
