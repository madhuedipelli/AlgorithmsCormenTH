def InsertionSort(A):
    """Insertion sort:
    assume 1st element is sorted, begin from second element.
        if max of sorted is < current element continue.
        else
        traverse through sorted to find correct spot for the current element
    """
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        # if current element is smaller than sorted last element
        # move sorted last element to current element
        # continue till position is found
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        # place the key in its appropriate position
        A[j+1] = key
    print(A)
    return
A = [10,4,5,10,7]
InsertionSort(A)