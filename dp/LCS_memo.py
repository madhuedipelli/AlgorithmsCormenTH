X = "abcdghemln"
Y = "abedfhrem"
m = len(X)
n = len(Y)
t = [[-1 for i in range(n+1)] for j in range(m+1)]

def LCS_memo(str1,str2,l1,l2):
    #Base Case Smallest valid common subsequence return length
    if l1 == 0 or l2 == 0:
        return 0
    if t[l1][l2] != -1:
        return t[l1][l2]
    if str1[l1-1] == str2[l2-1]:
        t[l1][l2]= 1+LCS_memo(str1,str2,l1-1,l2-1)
        return t[l1][l2]
    else:
        t[l1][l2]= max(LCS_memo(str1,str2,l1-1,l2),LCS_memo(str1,str2,l1,l2-1))
        return t[l1][l2]
print(LCS_memo(X,Y,m,n))