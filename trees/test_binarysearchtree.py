from binarysearchtree import BinarySearchTree

test = BinarySearchTree()

# for i in range(10):
#     test.put(i,i*i)
#     print(test.search(i))
#     print(f'search key = {i} , search val = {test.search(i)} , max is {test.get_max()} and min is {test.get_min()}')

test.put(12)
test.put(7)
test.put(3)
print(f'size is {test.size()}')
test.put(5)
test.put(4)
print(f'size is {test.size()}')

print(f'rank of 12 is {test.rank(12)}')

print(test.floor(6))
print(test.ceil(6))


test.inorder()
print()
test.preorder()
print()
test.postorder()
print()