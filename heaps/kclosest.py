import heapq
arr = [5,6,7,8,9]
x=7
k=1
""""
    find k closest elements in the array for given value x
"""
li = list()
out = list()

for i in arr:
    heapq.heappush(li,(-1*abs(i-x),i))
    if len(li)>k:
        heapq.heappop(li)
while len(li):
    out.append(heapq.heappop(li)[1])
print(out)