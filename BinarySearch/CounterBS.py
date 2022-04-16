def BSL(A,l,r,x,flag):
    res = -1
    while l <=r :
        mid = l + (r-l)//2
        if A[mid] > x:
            r = mid -1
        elif A[mid] < x:
            l = mid + 1
        else:
            res = mid
            if flag:
                r = mid-1
            else:
                l = mid + 1
    return res
def firstAndLast(A,n,x):
    l = 0
    r = n -1
    low = BSL(A,l,r,x,True)
    high = BSL(A,l,r,x,False)
    return high-low +1

A = [2,8,9,9,9,10,11]
n = len(A)
x = 9
print(firstAndLast(A,n,x))