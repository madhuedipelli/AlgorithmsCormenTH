class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self,key,val,count=0):
            self.key = key
            self.val = val 
            self.left = None
            self.right = None
            self.count = count

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
            return self.Node(key,val,1)
        
        if key < x.key :
            x.left = self.put_helper(x.left, key, val)
        
        elif key > x.key :
            x.right = self.put_helper(x.right, key, val)
        else:
            x.val = val
        x.count = 1 + self.size_helper(x.left) + self.size_helper(x.right)
        return x
    
    def get_min(self):
        x = self.get_min_helper(self.root)
        if x is None:
            return None
        return x.key
    def get_min_helper(self, x):
        if x is None:
            return None
        elif x.left is None:
            return x
        return self.get_min_helper(x.left)
        
        
    
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
    
    # in the interest of time lets print inorder here
    # return queue iterable in the next iteration
    def inorder(self):
        self.inorder_helper(self.root)
    
    def inorder_helper(self,x):
        if x is None:
            return
        self.inorder_helper(x.left)
        print(x.key, end = ' ')
        self.inorder_helper(x.right)
    
    def preorder(self):
        self.preorder_helper(self.root)
    
    def preorder_helper(self,x):
        if x is None:
            return
        print(x.key, end = ' ')
        self.preorder_helper(x.left)
        self.preorder_helper(x.right)
    
    def postorder(self):
        self.postorder_helper(self.root)
    
    def postorder_helper(self,x):
        if x is None:
            return
        self.postorder_helper(x.left)
        self.postorder_helper(x.right)
        print(x.key,end=' ')
    
    def size(self):
        return self.size_helper(self.root)
    
    def size_helper(self,x):
        if x is None:
            return 0
        return x.count
    
    def rank(self, key):
        return self.rank_helper(self.root, key)
    
    def rank_helper(self, x, k):
        if x is None:
            return 0
        if k < x.key :
            return self.rank_helper(x.left,k)
        elif k > x.key :
            return 1 + self.size_helper(x.left) + self.rank_helper(x.right, k)
        else:
            return self.size_helper(x.left)
    
    def deleteMin(self):
        self.root = self.deleteMin_helper( self.root )
    
    def deleteMin_helper(self, x):
        if x.left is None:
            return x.right
        x.left = self.deleteMin_helper(x.left)
        x.count = 1 + self.size_helper(x.left) + self.size_helper(x.right)
        return x
    
    def delete(self, key):
        self.root = self.delete_helper(self.root, key)

    def delete_helper(self, x, k):
        if x is None:
            return None
        if k < x.key :
            x.left = self.delete_helper(x.left, k)
        elif k > x.key :
            x.right = self.delete_helper(x.right, k)
        else:
            if x.right == None:
                return x.left
            if x.left == None:
                return x.right
            
            t = x
            #successor is used here
            # predecessor with t.left max will work as well
            x = self.get_min_helper(t.right)
            x.right = self.deleteMin_helper(t.right)
            x.left = t.left

            x.count = self.size_helper(x.left) + self.size_helper(x.right) + 1
            return x
    
        

"""
Notes:
Hibbard deletion is asymmetric, meaning after random 100N puts and may be
50N deletes , tree will become unbalanced and ops would cost sqrtN instead
of logN per op.
"""