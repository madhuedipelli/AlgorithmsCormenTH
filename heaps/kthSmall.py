import heapq
# python heapq is min heap
# so values are complemented with -1 for reversal
# as in 1000 becomes -1000 
li = []
heapq.heapify(li)
arr = [7,10,4,3,20,15]
k = 5
for i in arr:
    heapq.heappush(li,i*-1)
    #maintain heap size equal to k
    if len(li)>k:
        heapq.heappop(li)
print((heapq.heappop(li))*-1)