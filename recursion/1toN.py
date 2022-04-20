def Print(n):
    if n == 0:
        return
    Print(n-1)
    print(n,end=" ")
Print(10)
print()