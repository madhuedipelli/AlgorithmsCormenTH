def MinIndex(arr):
    n = len(arr)
    left = 0
    right = n-1
    
    while left <= right:
        mid = left + (right-left)//2
        after =( mid + 1)%n
        before = (mid -1 + n)%n
        if arr[mid] <= arr[after] and arr[mid] <= arr[before]:
            return mid
        elif arr[left] < arr[mid]:
            left = mid-1
        elif arr[right] > arr[mid]:
            right = mid+1
        else:
            return 0
def BinarySearch(arr,left,right,key):
    if not arr:
        return -1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid-1
        else:
            left = mid + 1
    return -1
def NumSortedRotated(arr,target):
    index = MinIndex(arr)
    out = BinarySearch(arr,0,index-1,target)
    out2 = BinarySearch(arr,index,len(arr)-1,target)
    return max(out,out2)
A =[5,1,2,3,4]
print(NumSortedRotated(A,5))