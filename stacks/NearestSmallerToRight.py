def NearestSmallerToRight(arr,n):
    out = list()
    stack = list()

    for j in range(n-1,-1,-1):

        if len(stack) == 0:
            out.append(-1)
        elif stack[-1] < arr[j]:
            out.append(stack[-1])
        else:
            while len(stack) > 0 and stack[-1] >= arr[j]:
                stack.pop()
            if len(stack) == 0:
                out.append(-1)
            else:
                out.append(stack[-1])
        stack.append(arr[j])
    return out[::-1]
A = [1,3,2,4]
n = len(A)
print(NearestSmallerToRight(A,n))