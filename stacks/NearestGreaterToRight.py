""""Question:
    Given an array arr[ ] of size N having distinct elements,
    the task is to find the next greater element for each element of the array in order of their appearance in the array.
    Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
    If there does not exist next greater of current element, then next greater element for current element is -1.
    For example, next greater of the last element is always -1.
    input = [1 3 2 4], output = [3 4 4 -1].
    refer gfg : Next Greater Element 
"""

def NearestGreaterToRight(arr,n):
    #code here
    out = list()
    stack = list()
    
    for j in range(n-1,-1,-1):
        if len(stack) == 0:
            out.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[j]:
            out.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[j]:
            while len(stack)>0 and stack[-1] <= arr[j]:
                stack.pop()
            if len(stack) > 0:
                out.append(stack[-1])
            else:
                out.append(-1)
        stack.append(arr[j])
    return out[::-1]
A = [1, 3 ,2 ,4]
n = len(A)
print(NearestGreaterToRight(A,n))