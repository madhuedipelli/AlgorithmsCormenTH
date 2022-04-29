import heapq

arr = [1,2,3,4,5]
li = list()

for i in arr:
    heapq.heappush(li,i)

tSum = 0
while len(li)>1:
    x = heapq.heappop(li)
    x +=heapq.heappop(li)
    tSum += x
    heapq.heappush(li,x)

print(tSum)