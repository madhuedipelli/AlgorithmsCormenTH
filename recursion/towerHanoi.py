def towerOfHanoi(n, src, dest, aux):
    if n == 1:
        print("move disk 1 from pole source : {}\
             to destination : {}".format(src, dest))
        return
    towerOfHanoi(n - 1, src, aux, dest)
    print("move disk {} from source : {} to destination : {}".format(n, src, dest))
    towerOfHanoi(n - 1, aux, src, dest)


n = input("Enter integer less than 10 : ")
towerOfHanoi(int(n), 'A', 'B', 'C')
