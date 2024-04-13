from binarysearchtree import BinarySearchTree

test = BinarySearchTree()

# for i in range(2,10):
#     test.put(i,i*i)
#     print(test.search(i))
#     print(f'search key = {i} , search val = {test.search(i)} , max is {test.get_max()} and min is {test.get_min()}')

# test.deleteMin()
# print(f'min is {test.get_min()}')

# print(f'search for 6 before delete : {test.search(6)}')
# test.delete(6)
# print(f'search for 6 after delete : {test.search(6)}')

test.put(12,"some")
test.put(13)
test.put(7)
test.put(3)

test.inorder()
print()
print(f'search for 12 before delete : {test.search(12)}')
test.delete(12)

test.inorder()
print()
print(f'size is {test.size()}')
test.put(5)
test.put(4)
print(f'size is {test.size()}')

print(f'search for 12 after delete : {test.search(12)}')
print(f'rank of 12 is {test.rank(12)}')

print(test.floor(6))
print(test.ceil(6))

test.inorder()
print()
test.preorder()
print()
test.postorder()
print()