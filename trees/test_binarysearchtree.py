from binarysearchtree import BinarySearchTree

test = BinarySearchTree()

# for i in range(10):
#     test.put(i,i*i)
#     print(test.search(i))
#     print(f'search key = {i} , search val = {test.search(i)} , max is {test.get_max()} and min is {test.get_min()}')

test.put(12)
test.put(7)
test.put(3)
test.put(5)
test.put(4)

print(test.floor(6))
print(test.ceil(6))