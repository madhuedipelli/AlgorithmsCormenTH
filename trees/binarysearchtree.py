class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val 
            self.left = None
            self.right = None

    def search(self,key):
        out = self.search_helper(self.root, key)
        if out is not None:
            return out.val
        else:
            return None

    def search_helper(self, x, k):
        if x is None:
            return None
        if x.key == k:
            return x
        elif x.key > k:
            return self.search_helper(x.left,k)
        else:
            return self.search_helper(x.right,k)
    
    def put(self,key,val):
        self.root = self.put_helper(self.root,key,val)

    def put_helper(self,x,key,val):
        if x == None:
            return self.Node(key,val)
        
        if key < x.key :
            x.left = self.put_helper(x.left, key, val)
        
        elif key > x.key :
            x.right = self.put_helper(x.right, key, val)
        else:
            x.val = val
        
        return x

