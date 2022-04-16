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
        elif arr[mid] < key:
            right = mid-1
        else:
            left = mid + 1
    return -1
arr=[299, 263, 141, 128, 119, 102, 87, 66, 60, 53, 50, 48]
print(BinarySearch(arr,48))