from binarysearchtree import BinarySearchTree

test = BinarySearchTree()

for i in range(10):
    test.put(i,i*i)

for i in range(10):
    print(test.search(i), end = ' ')