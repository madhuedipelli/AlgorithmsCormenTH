import heapq

arr = [(1,3),(-2,2),(5,8),(0,1)]
k = 3
li = list()

for i in arr:
    d = (i[0]**2 + i[1]**2)

    heapq.heappush(li,(-1*d,i))
    if len(li) >k:
        heapq.heappop(li)
while len(li):
    print(heapq.heappop(li)[1],end=" ")
print()

"""
k closest points to origin,
find distance, take max heap and pop off 
all max distance points  each time heap.length > k
"""