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
    heapq.heappush(li,(value,key))
    if len(li)>k:
        heapq.heappop(li)
while len(li):
    print(heapq.heappop(li)[1],end=" ")
print()

"""
ps:give top k frequent elements in the array
"""
"""
soln: use hash to make frquency counter and
      heap to give k top elements.
      min heap pops out min elements so heap
      will maintain max.
"""