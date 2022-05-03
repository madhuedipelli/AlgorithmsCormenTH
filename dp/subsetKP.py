def subsetCount(arr,S):
    n=len(arr)
    t = [[None for j in range(S+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(S+1):
            if (i == 0 and j==0) or j==0:
                t[i][j] = 1
            elif i==0 :
                t[i][j] = 0
    for i in range(1,n+1):
        for j in range(1,S+1):
            if arr[i-1] <= S:
                t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print(t[n][S])
arr = [2,3,5,6,8,10]
S = 6
subsetCount(arr,S)