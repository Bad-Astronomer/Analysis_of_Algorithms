# 0/1 knapsack using dynamic programming

def knapsack(W, wt, val, n):
    if n==0 or W==0: #no item or remaining capacity = 0
        return 0
    
    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1) #exclude item if item weight > W
    
    else:
        return max(
            val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), #include item
            knapsack(W, wt, val, n-1) #exclude item
        )

profit = [100, 120, 150, 140]
weight = [10, 20, 40, 30]
W = 50
print(knapsack(W, weight, profit, len(profit)))