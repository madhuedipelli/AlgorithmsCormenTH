def Print(n):
    # prints from N to 1
    if n == 0:
        return
    print(n,end=" ")
    Print(n-1)
Print(10)
print()