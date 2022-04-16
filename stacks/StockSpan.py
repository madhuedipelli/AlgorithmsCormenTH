def StockSpan(A,n):
    out = list()
    stack = list()
    temp = list()
    for j in range(n):
        print(stack)
        if len(stack)==0 or stack[-1]>A[j]:
            out.append(1)
        else:
            count = 1
            while len(stack) > 0 and stack[-1] <= A[j]:
                count += 1
                temp.append(stack.pop())
            while temp:
                stack.append(temp.pop())
            out.append(count)
        stack.append(A[j])
    return out

A = [100,80,60,70,60,75,85]
n = len(A)

print(StockSpan(A,n))