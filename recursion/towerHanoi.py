def Print(fro,to):
    print("moved  from {} to {}".format(fro,to))

def towerHanoi(n,frm,to,spare):
    if n == 1:
        Print(frm,to)
    else:
        towerHanoi(n-1,frm,spare,to)
        towerHanoi(1,frm,to,spare)
        towerHanoi(n-1,spare,to,frm)
        print()
towerHanoi(4,"from","to","spare")