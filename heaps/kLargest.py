import heapq
arr = [7,10,4,3,20,15]
k = 4
# return list of k largest elements in the given array
# uses min heap
# min heap pop deletes min element each time len(heap) > k
# thereby maintaining heap of largest elements only of length k.
li = list()

for i in arr:
    heapq.heappush(li,i)
    if len(li) > k:
        heapq.heappop(li)

out = [heapq.heappop(li) for i in range(k)]
print(out)