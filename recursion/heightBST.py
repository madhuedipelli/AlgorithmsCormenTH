class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

def height(root):
    if root == None:
        return 0
    left = height(root.left)
    right = height(root.right)

    return max(left,right) + 1
print(height(root))