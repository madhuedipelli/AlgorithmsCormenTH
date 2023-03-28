def tower_of_hanoi(num, src, dest, aux):
    """
    key points:
    for n disks on A,n-1 disks are moved from A to C
    nth disk is moved from A to B
    now the problem becomes length n-1,
    src as C, dst as B and aux as A and so on.
    """
    if num == 1:
        print("move disk 1 from pole source : {}\
             to destination : {}".format(src, dest))
        return
    tower_of_hanoi(num - 1, src, aux, dest)
    print("move disk {} from source : {} to destination : {}".format(num, src, dest))
    tower_of_hanoi(num - 1, aux, dest, src)


n = input("Enter integer less than 10 : ")
tower_of_hanoi(int(n), 'A', 'B', 'C')
