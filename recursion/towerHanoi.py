
count = 0
def Movetower(n,src,dest,aux):

    if n > 0:
        Movetower(n-1,src,aux,dest)    # move n-1 disks to aux pole
        MoveSingleDisk(n,src,dest)     # move mth disk to dest from src
        Movetower(n-1,aux,dest,src)    # start the recursion for remaining n-1 elements

def MoveSingleDisk(n,src,dest):
    global count
    count += 1
    print(f'Moving {n} from {src} to {dest}')

Movetower(20,'A','B','temp')
print(count)
