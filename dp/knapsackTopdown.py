wt=[1,3,4,5]
val=[1,4,5,12]
W=7
n=len(wt)-1

def knapsack(wt,val,W,n):
    t = [[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j] = 0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1] <= W:
                t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][W]
print(knapsack(wt,val,W,n))