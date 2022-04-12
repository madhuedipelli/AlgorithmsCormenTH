def LEFT(idx):
    return 2*idx
def RIGHT(idx):
    return 2*idx + 1

def Max_Heapify(A,idx):
    if idx > len(A):
        return
    left = LEFT(idx)+1
    right = RIGHT(idx)+1
    print(left,right)
    if left < len(A) and A[left] > A[idx]:
        largest = left
    else:
        largest = right
    if largest !=idx and largest < len(A):
        A[largest],A[idx] = A[idx],A[largest]
        Max_Heapify(A,largest)
    return A

A=[16,4,10,14,7,2,8,1,9,3]
print(Max_Heapify(A,1))