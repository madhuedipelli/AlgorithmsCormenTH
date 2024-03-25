def count_inversions(arr):
    ''' simple brute force'''
    inv_cnt = 0

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr [j]:
                inv_cnt += 1
    return inv_cnt

print(count_inversions([6,5,4,3,2,1]))
