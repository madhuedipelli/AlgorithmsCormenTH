X = "ABCDGH"
Y = "ACDGHR"
m = len(X)-1
n = len(Y)-1

def RecursiveLongestCommonSubSequence(str1,str2,l1,l2):
    
    #Base Case Smallest valid common subsequence return length
    if l1 == 0 or l2 == 0:
        return 0
    if str1[l1-1] == str2[l2-1]:
        return 1+RecursiveLongestCommonSubSequence(str1,str2,l1-1,l2-1)
    else:
        return max(RecursiveLongestCommonSubSequence(str1,str2,l1-1,l2),RecursiveLongestCommonSubSequence(str1,str2,l1,l2-1))
print(RecursiveLongestCommonSubSequence(X,Y,m,n))
