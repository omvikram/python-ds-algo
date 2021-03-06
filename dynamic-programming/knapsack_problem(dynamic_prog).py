# Dynamic Programming recomputations of same subproblems can be avoided by constructing a temporary array K[][] 
# in bottom-up manner. In a DP[][] table let’s consider all the possible weights and capacity in columns and rows.


# A Dynamic Programming based Python  
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity C

def knapSack(C, wt, val, n): 
    K = [[0 for x in range(C + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(C + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][C] 
  
# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
C = 50
n = len(val) 
print(knapSack(C, wt, val, n)) 

# Time Complexity: O(N*W)
# As redundant calculations of states are avoided.