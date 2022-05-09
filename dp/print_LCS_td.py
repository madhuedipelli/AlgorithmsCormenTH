X = "ABCDGH"
Y = "ACDGHR"
m = len(X)-1
n = len(Y)-1


def LCS_topDown(str1,str2,m,n):
    #Base Case Smallest valid common subsequence return length
    t = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else :
                t[i][j] = max(t[i-1][j],t[i][j-1])
    a,b=m,n
    out = ""
    while a >= 0 and b >= 0:
        if str1[a-1] == str2[b-1]:
            out += str1[a]
            a -= 1
            b -= 1
        else:
            if t[a-1][b] > t[a][b-1]:
                a -= 1
            else:
                b -= 1
    return out[::-1]
print(LCS_topDown(X,Y,m,n))