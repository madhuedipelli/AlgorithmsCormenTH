wt=[1,3,4,5]
val=[1,4,5,12]
W=7
n=len(wt)-1

def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if wt[n] <= W:
        return max(val[n]+knapsack(wt,val,W-wt[n],n-1),
        knapsack(wt,val,W,n-1))
    else:
        return knapsack(wt,val,W,n-1)
print(knapsack(wt,val,W,n))