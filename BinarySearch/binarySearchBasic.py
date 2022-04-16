import random
def BinarySearch(arr,key):
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid-1
        else:
            left = mid + 1
    return -1
arr = [48, 50, 53, 60, 66, 87, 102, 119, 128, 141, 263, 299]
print(BinarySearch(arr,299))