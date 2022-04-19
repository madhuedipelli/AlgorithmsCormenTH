
def subsetUtil(ip,output,out):
    if len(ip) ==0:
        return output.append(out)
    subsetUtil(ip[:len(ip)-1],output,out)
    out += ip[-1]
    subsetUtil(ip[:len(ip)-1],output,out)
    return output
def subset(ip):
    output=[]
    out = ""
    output = subsetUtil(ip,output,out)
    return output

A="abcdefg"
print(subset(A))