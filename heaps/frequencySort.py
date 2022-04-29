import heapq
arr = [1,1,1,3,2,2,4]
k = 2
hashed = dict()
for i in arr:
    if i in hashed:
        hashed[i] += 1
    else:
        hashed[i] = 1
li = list()
for key,value in hashed.items():
    heapq.heappush(li,(-1*value,key))
x=0
while len(li):
    freq,val=heapq.heappop(li)
    for i in range(-1*freq):
        arr[x]=val
        x+=1
print(arr)