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
    
    def put(self,key,val=None):
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
    
    def get_min(self):
        if self.root is None :
            return None
        x = self.root
        while x.left != None:
            x = x.left
        return x.key
    
    def get_max(self):
        if self.root is None:
            return None
        x = self.root
        while x.right is not None:
            x = x.right
        return x.key
    
    def floor(self, key):
        x = self.floor_helper(self.root, key)
        if x is None:
            return None
        return x.key
    
    def floor_helper(self, x, k):
        if x is None:
            return None
        
        if x.key == k:
            return x
        
        if x.key > k :
            return self.floor_helper(x.left, k)
        # either x is floor or x right subtree has k's floor
        # not left subtree
        t = self.floor_helper(x.right, k)
        if t is None:
            return x
        else:
            return t
    
    def ceil(self,key):
        x = self.ceil_helper(self.root, key)
        if x :
            return x.key
        else:
            return None
    
    def ceil_helper(self, x, k):
        if x is None:
            return None
        if x.key == k:
            return x
        
        if x.key < k:
            return self.ceil_helper(x.right, k)
        
        # k's ceil is current x or 
        # leftmost child in current x

        t = self.ceil_helper(x.left, k)
        if t is None:
            return x
        return t