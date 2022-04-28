import heapq
arr = [6,5,3,2,8,10,9]
k = 4
li = list()
out = list()
""" 
    nearly or k sorted array where element corresponding to index 
    will be in k range
"""
for i in range(len(arr)):
    heapq.heappush(li,arr[i])
    if len(li)>k:
        out.append(heapq.heappop(li))
for i in range(k):
    out.append(heapq.heappop(li))
print(out)
