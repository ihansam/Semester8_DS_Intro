#1. Linked-Based BST
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key    = key
        self.value  = value
        self.left   = left
        self.right  = right

class BST:                      # Linked Structure Binary Search Tree
    def __init__(self):         # Empty BST initialize
        self.root = None        

    # [SEARCH]
    def get(self, k):           # get value of key
        return self._get_item(self.root, k) # search from the root node

    def _get_item(self, n, k):  # compare the node & key
        if n == None:           # No such Key in the BST
            return None
        if n.key > k:           # smaller key, go left
            return self._get_item(n.left, k)
        elif n.key < k:         # larger key, go right
            return self._get_item(n.right, k)
        else:                   # target key found
            return n.value      # return value of the node

    # [INSERT]
    def put(self, k, v):        # put a new node to BST
        self.root = self._put_item(self.root, k, v)   # search place from root

    def _put_item(self, n, key, value):
        if n == None:                   # found inserting place
            return Node(key, value)     # => insert new node
        if n.key > key:                 # smaller key, go left
            n.left = self._put_item(n.left, key, value)
        elif n.key < key:               # larger key, go right
            n.right = self._put_item(n.right, key, value)
        else:                           # already key exist
            n.value = value             # => just update value
        return n                        # return the node

    # [DELETE]
    def min(self):          # find min node
        if self.root == None:
            return None
        return self._minimum(self.root) # find from root

    def _minimum(self, n):  # private method
        if n.left == None:  # min node found
            return n
        return self._minimum(n.left)    # else go left

    def delete_min(slef):   # delete minumum node in the tree
        if self.root == None:
            print("Tree is Empty")
        self.root = self._del_min(self.root)    # search from the root
        
    def _del_min(self, n):  # private method
        if n.left == None:  # n don't have left child => n is min node
            return n.right  # replace n = n.right
        n.left = self._del_min(n.left)  # n has left child => go left
        return n

    def delete(self, k):            # delete node by key
        self.root = self._del_node(self.root, k)    # search from root
    
    def _del_node(self, n, k):
        if n == None:               # node search fail
            return None
        if n.key > k:               # smaller target, go left
            n.left = self._del_node(n.left, k)
        elif n.key < k:             # bigger target, go right
            n.right = self._del_node(n.right, k)
        else:                       # target found
            if n.right == None:     # no child & only left child case
                return n.left       # => connect left subtree
            if n.left == None:      # only right child case
                return n.right      # => connect right subtree
            target = n              # both child exist case
            n = self._minimum(target.right) # replace target to successor node  
            n.right = self._del_min(target.right)   # connect right w/o n
            n.left = target.left                    # connect left
        return n
    
    # [Treversal]
    def preorder(self):
        self._preorder(self.root)   # start from the root
        print()

    def _preorder(self, n): # private
        if n != None:       # if not empty, print root first
            print(str((n.key, n.value)), end=" ")
            if n.left:      # print left
                self._preorder(n.left)
            if n.right:     # print right
                self._preorder(n.right)
    
    def postorder(self):
        self._postorder(self.root)  # start from the root
        print()

    def _postorder(self, n):    # private
        if n != None:           # if not empty,
            if n.left:          # print left first,
                self._postorder(n.left)
            if n.right:         # and right, and the root
                self._postorder(n.right)
            print(str((n.key, n.value)), end=" ")

    def inorder(self):
        self._inorder(self.root)    # start from the root
        print()

    def _inorder(self, n):      # private
        if n != None:           # if not empty
            if n.left:          # print left first, and root,
                self._inorder(n.left)
            print(str((n.key, n.value)), end=" ")
            if n.right:         # and right
                self._inorder(n.right)

    def levelorder(self):
        self._levelorder(self.root) # start from the root
        print()

    def _levelorder(self, root):    # private
        q = []                      # Queue
        q.append(root)              # append the root node
        while len(q) != 0:          # iteration until the Queue is empty
            n = q.pop(0)            # travel first node in the Queue
            print(str((n.key, n.value)), end=" ")
            if n.left != None:      # insert node's left child if exist
                q.append(n.left)
            if n.right != None:     # insert node's right child if exist
                q.append(n.right)

def Check(lt):
    lt.put(10, 'P')
    lt.levelorder()
    lt.put(5, 'K')
    lt.levelorder()
    lt.put(15, 'U')
    lt.levelorder()
    lt.put(3, 'I')
    lt.levelorder()
    lt.put(17, 'W')
    lt.levelorder()
    lt.put(2, 'H')
    lt.levelorder()
    lt.put(19, 'Y')
    lt.levelorder()
    lt.put(4, 'J')
    lt.levelorder()
    lt.put(8, 'N')
    lt.levelorder()
    lt.put(9, 'O')
    lt.levelorder()
    lt.delete(5)
    lt.levelorder()
    lt.delete(3)
    lt.levelorder()
    lt.delete(17)
    lt.levelorder()
    print(lt.get(19))
    print(lt.get(8))
    lt.preorder()
    lt.postorder()
    lt.inorder()
    lt.levelorder()

#2. Array-Based BST
def parent(n):          # return parent index
    if n>0:
        return int((n-1)/2)
    else:
        return None
    
def left(n):            # return left child index
    return 2*n+1

def right(n):           # return right child index
    return 2*n+2
   
class BST_ARRAY:
    def __init__(self):
        self._keydata = []          # key data
        self._valdata = []          # value data
        self._count = 0             # number of items
    
    def __str__(self):              # for check array elements
        return 'KEY: ' + str(self._keydata) + '\nVAL: ' + str(self._valdata)

    def isEmpty(self):              # check Empty or not
        return self._count == 0

    # [SEARCH]
    def get(self, k):               # search a value with key
        return self._get(k)[1]      # only return the value

    def _get(self, key):            # private search method
        idx = 0                     # search index
        while (True):
            try:                    # get key of index
                n = self._keydata[idx]
            except:                 # index overflow
                return None, None, idx  # => not exist
            if n == None:           # node is empty
                return n, None, idx     # => not exist
            elif n > key:           # smaller key, go left
                idx = left(idx)
            elif n < key:           # larger key, go right
                idx = right(idx)
            else:                   # key found, return (key, value, index)
                return n, self._valdata[idx], idx

    # [INSERT]
    def _sizeup(self):              # array size doubling method
        size = len(self._keydata)+1
        self._keydata += [None for _ in range(size)]
        self._valdata += [None for _ in range(size)]

    def put(self, key, value):              # insert method
        n, val, idx = self._get(key)        # find insert place
        while idx >= len(self._keydata):    # if overflow
            self._sizeup()                  # size doubling
        self._keydata[idx] = key            # key update
        self._valdata[idx] = value          # value update

"""
        idx = 0                     # search index
        done = False                # iteration Flag
        while (not done):
            try:                    # get key of idx
                n = self._keydata[idx]
            except:                 # indexing error
                self._sizeup()      # => need to size up
                continue
            if n == None:           # found inserting place
                self._keydata[idx] = key    
                self._valdata[idx] = value
                done = True
            elif n > key:           # smaller key, go left
                idx = left(idx)
            elif n < key:           # larger key, go right
                idx = right(idx)
            else:                   # already exist key
                self._valdata[idx] = value  # update value only
                done = True
"""
    # [DELETE]


def RunTimeAnalysis():
    pass

if __name__ == "__main__":
    bst_link = BST()
    Check(bst_link)
    bst_array = BST_ARRAY()
    print(bst_array.get(0))
    bst_array.put(11, "eleven")
    print(bst_array)
    bst_array.put(2, "two")
    print(bst_array)
    bst_array.put(3, "eight")
    print(bst_array)
    bst_array.put(3, "three")
    print(bst_array)

    print(bst_array.get(3))
    
    # Check(bst_array)
    RunTimeAnalysis()

