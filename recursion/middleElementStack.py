def utilMiddle(arr,k):
    if k == 1:
        arr.pop()
        return arr
    temp = arr.pop()
    arr=utilMiddle(arr,k-1)
    arr.append(temp)
    return arr
def deleteMiddle(arr):
    k = len(arr)//2 +1
    if k % 2 == 0:
        arr=utilMiddle(arr,k)
        arr=utilMiddle(arr,k-1)
    else:
        arr=utilMiddle(arr,k)
    return arr
arr=[2,3,1,4,5,6]

print(deleteMiddle(arr))