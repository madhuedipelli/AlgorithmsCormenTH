def NearestGreaterToLeft(arr,n):
    #code here
    out = list()
    stack = list()
    for j in range(n):
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
    return out
A = [1, 3 ,2 ,4]
n = len(A)
print(NearestGreaterToLeft(A,n))