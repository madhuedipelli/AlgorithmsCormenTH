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
            if arr[i-1] <= j:
                t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print(t[n][S])
# code for difference subset sum count
# s1 - s2 = diff
# s1 + s2 = sum(arr) on solving both
arr = [1,1,2,3]
diff = 1
s1 = (diff + sum(arr))//2
subsetCount(arr,s1)