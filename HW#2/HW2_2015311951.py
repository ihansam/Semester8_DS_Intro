# Data Structure HW#2, SKKU EEE Kidan Jin
#1. Linked-Based BST
# [Node Class]
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key    = key
        self.value  = value
        self.left   = left
        self.right  = right

# [BST Class]
class BST:                      # Linked Structure Binary Search Tree
    def __init__(self):         # Empty BST initialize
        self.root = None        

    # [SEARCH]
    def get(self, k):           # get value of key
        return self.__get_item(self.root, k)    # search from the root

    def __get_item(self, n, k): # compare the node & key
        if n == None:           # No such Key in the BST
            return None
        if n.key > k:           # smaller key, go left
            return self.__get_item(n.left, k)
        elif n.key < k:         # larger key, go right
            return self.__get_item(n.right, k)
        else:                   # target key found
            return n.value      # return value of the node

    # [INSERT]
    def put(self, k, v):        # put a new node to BST
        self.root = self.__put_item(self.root, k, v)    # search from root

    def __put_item(self, n, key, value):
        if n == None:                   # found inserting place
            return Node(key, value)     # => insert new node
        if n.key > key:                 # smaller key, go left
            n.left = self.__put_item(n.left, key, value)
        elif n.key < key:               # larger key, go right
            n.right = self.__put_item(n.right, key, value)
        else:                           # already key exist
            n.value = value             # => just update value
        return n                        # return the node

    # [DELETE]
    def min(self):          # find min node
        if self.root == None:
            return None
        return self.__minimum(self.root)    # find from root

    def __minimum(self, n): # private method
        if n.left == None:  # min node found
            return n
        return self.__minimum(n.left)       # else go left

    def delete_min(self):   # delete minumum node in the tree
        if self.root == None:
            print("Tree is Empty")
        self.root = self.__del_min(self.root)   # search from the root
        
    def __del_min(self, n): # private method
        if n.left == None:  # n don't have left child => n is min node
            return n.right  # replace n = n.right
        n.left = self.__del_min(n.left) # n has left child => go left
        return n

    def delete(self, k):            # delete node by key
        self.root = self.__del_node(self.root, k)   # search from root
    
    def __del_node(self, n, k):
        if n == None:               # node search fail
            return None
        if n.key > k:               # smaller target, go left
            n.left = self.__del_node(n.left, k)
        elif n.key < k:             # bigger target, go right
            n.right = self.__del_node(n.right, k)
        else:                       # target found
            if n.right == None:     # no child & only left child case
                return n.left       # => connect left subtree
            if n.left == None:      # only right child case
                return n.right      # => connect right subtree
            target = n              # both child exist case
            n = self.__minimum(target.right)        # replace target to successor node  
            n.right = self.__del_min(target.right)  # connect right w/o n
            n.left = target.left                    # connect left
        return n
    
    # [Treversal]
    def preorder(self):
        self.__preorder(self.root)  # start from the root
        print()

    def __preorder(self, n):
        if n != None:       # if not empty, print root first
            print(str((n.key, n.value)), end=" ")
            if n.left:      # print left
                self.__preorder(n.left)
            if n.right:     # print right
                self.__preorder(n.right)
    
    def postorder(self):
        self.__postorder(self.root) # start from the root
        print()

    def __postorder(self, n):   
        if n != None:           # if not empty,
            if n.left:          # print left first,
                self.__postorder(n.left)
            if n.right:         # and right, and the root
                self.__postorder(n.right)
            print(str((n.key, n.value)), end=" ")

    def inorder(self):
        self.__inorder(self.root)   # start from the root
        print()

    def __inorder(self, n):     
        if n != None:           # if not empty
            if n.left:          # print left first, and root,
                self.__inorder(n.left)
            print(str((n.key, n.value)), end=" ")
            if n.right:         # and right
                self.__inorder(n.right)

    def levelorder(self):
        self.__levelorder(self.root)# start from the root
        print()

    def __levelorder(self, root):   
        q = []                      # Queue
        if (root != None):          # append the root if not None
            q.append(root)          
        while len(q) != 0:          # iteration until the Queue is empty
            n = q.pop(0)            # travel first node in the Queue
            print(str((n.key, n.value)), end=" ")
            if n.left != None:      # insert node's left child if exist
                q.append(n.left)
            if n.right != None:     # insert node's right child if exist
                q.append(n.right)

# [Test Procedure]
def Check(BST):
    indata = [(10,'P'),(5,'K'),(15,'U'),(3,'I'),(17,'W'),\
            (2,'H'),(19,'Y'),(4,'J'),(8,'N'),(9,'O')]
    for key, value in indata:
        BST.put(key, value)
        BST.levelorder()
    outdata = [(5,'K'), (3,'I'), (17,'W')]
    for key, value in outdata:
        BST.delete(key)
        BST.levelorder()
    print(BST.get(19))
    print(BST.get(8))
    BST.preorder()
    BST.postorder()
    BST.inorder()
    BST.levelorder()

#2. Array-Based BST
# [node index functions]
def parent(n):          # return parent index
    if n>0:
        return int((n-1)/2)
    else:
        return None
    
def left(n):            # return left child index
    return 2*n+1

def right(n):           # return right child index
    return 2*n+2

# [BST Class]
class BST_ARRAY:
    def __init__(self):
        self.__keydata = []         # key data array
        self.__valdata = []         # value data array
    
    def __str__(self):              # for check array elements
        return 'KEY: ' + str(self.__keydata) + '\nVAL: ' + str(self.__valdata)

    def isEmpty(self):              # check Empty or not
        try:                        # by check root key
            return self.__keydata[0] == None
        except:                     # root not exist
            return True

    # [SEARCH]
    def get(self, k):               # search a value with key
        return self.__find(k)[1]    # only return the value

    def __find(self, key):          # private search method
        idx = 0                     # search index
        while (True):
            try:                    # get key of index
                n = self.__keydata[idx]
            except:                 # index overflow
                return None, None, idx  # => not exist
            if n == None:           # node is empty
                return n, None, idx     # => not exist
            elif n > key:           # smaller key, go left
                idx = left(idx)
            elif n < key:           # larger key, go right
                idx = right(idx)
            else:                   # key found, return (key, value, index)
                return n, self.__valdata[idx], idx

    # [INSERT]
    def __sizeup(self):             # array size doubling method
        size = len(self.__keydata)+1
        self.__keydata += [None for _ in range(size)]
        self.__valdata += [None for _ in range(size)]

    def put(self, key, value):              # insert method
        n, val, idx = self.__find(key)      # find insert place
        while idx >= len(self.__keydata):   # if overflow
            self.__sizeup()                 # size doubling
        self.__keydata[idx] = key           # key update
        self.__valdata[idx] = value         # value update

    # [DELETE]
    def __nodePromote(self, where, to): # node promote recursively
        key = self.__keydata[where]     # save where node 
        val = self.__valdata[where]       
        self.__keydata[to] = key        # replace to node
        self.__valdata[to] = val         
        self.__keydata[where] = None    # delete where node
        self.__valdata[where] = None
        if (left(where) < len(self.__keydata)): # next depth exist check
            if(self.__keydata[left(where)] != None):    # go left if exist
                self.__nodePromote(left(where), left(to))
            if(self.__keydata[right(where)] != None):   # go right if exist
                self.__nodePromote(right(where), right(to))

    def __minimum(self, start):         # find minimun node
        idx = start                     # from start index
        if self.__keydata[idx] == None: # Empty case return
            return None
        size = len(self.__keydata)      # until meet None or Undefined node
        while (idx < size and self.__keydata[idx] != None):
            idx = left(idx)             # go left
        return parent(idx)              # and return index

    def delete(self, key):              # delete node by key
        n, v, idx = self.__find(key)    # find delete node
        if n == key:                    # if delete node exist
            if (left(idx) >= len(self.__keydata)):  # child undefined case
                self.__keydata[idx] = None          # => just delete
                self.__valdata[idx] = None
            elif (self.__keydata[left(idx)] == None):   # left child empty
                self.__nodePromote(right(idx), idx)     # => right child Promote
            elif (self.__keydata[right(idx)] == None):  # right child empty
                self.__nodePromote(left(idx), idx)      # => left child Promote
            else:
                successor = self.__minimum(right(idx))  # find successor index
                self.__keydata[idx] = self.__keydata[successor] # replace
                self.__valdata[idx] = self.__valdata[successor]
                self.__keydata[successor] = None                # and delete
                self.__valdata[successor] = None                # the successor
                try:    # if successor has right child, promote right subtree
                    if(self.__keydata[right(successor)] != None):
                        self.__nodePromote(right(successor), successor)
                except:
                    pass
    
    # [Treversal]
    def preorder(self):
        self.__preorder(0)              # start from root
        print()
    
    def __preorder(self, i):
        try:
            n = self.__keydata[i]       # get i-th key
        except:                         
            return                      # not exist => return
        if n!= None:                    # None => return
            print(str((n, self.__valdata[i])), end=" ") # travel root
            self.__preorder(left(i))                    # left child
            self.__preorder(right(i))                   # right child

    def inorder(self):
        self.__inorder(0)               # start from root
        print()

    def __inorder(self, i):
        try:
            n = self.__keydata[i]       # get i-th key
        except:                         
            return                      # not exist => return
        if n!= None:                    # None => return
            self.__inorder(left(i))                     # left child
            print(str((n, self.__valdata[i])), end=" ") # travel root
            self.__inorder(right(i))                    # right child

    def postorder(self):
        self.__postorder(0)             # start from root
        print()

    def __postorder(self, i):
        try:                            
            n = self.__keydata[i]       # get i-th key
        except:                         
            return                      # not exist => return
        if n!= None:                    # None => return
            self.__postorder(left(i))                   # left child
            self.__postorder(right(i))                  # right child
            print(str((n, self.__valdata[i])), end=" ") # travel root

    def levelorder(self):
        if not self.isEmpty():          # Empty Check
            for key, value in zip(self.__keydata, self.__valdata):
                if key != None:         # travel not None keys sequentially
                    print(str((key, value)), end=" ")
        print()

#3. Running time Analysis
from time import time
from random import randint as rand

def run(bst, n, shuffle):
    # make n elements BST
    if shuffle:     # random case, random dataset
        for i in range(n):
            bst.put(rand(0, 2*n), 0)
    else:           # worst case, sequential dataset
        for i in range(n):
            bst.put(2*i, 0)

    # average INSERT time (ns)
    num = 10        # number of tries
    s = time()
    if shuffle:     # random case, random insert
	    for i in range(num):
	        bst.put(rand(0, 2*n), 0)
    else:           # worst case, sequential insert
        for i in range(num):
            bst.put(2*(n+i), 0)
    e = time()
    intime = int((e-s)/num*1000000000)

    # average SEARCH time (ns)
    s = time()
    for i in range(num):    # random search
        bst.get(rand(0, 2*n))
    e = time()
    stime = int((e-s)/num*1000000000)

    # aveage DELETE time (ns)
    s - time()
    for i in range(num):    # random delete
        bst.delete(rand(0, 2*n))
    e = time()
    dtime = int((e-s)/num*1000000000)

    # print results
    print("n = ", n, " Insert: ", intime, " Search: ", stime, " Delete: ", dtime)

def RunTimeAnalysis():
    print("[Worst Case]")
    print("{Linked-based}")
    for i in range(0, 7, 1):
        n = 10*(2**i)
        bstlnk = BST()          # linked-based BST
        run(bstlnk, n, False)   # worst case
    print("{Array-based}")
    for n in range(10, 20, 1):
        bstarr = BST_ARRAY()    # array-based BST
        run(bstarr, n, False)   # worst case
    print("[Common Case]")
    print("{Linked-based}")
    for i in range(4, 12, 1):
        n = 2**i
        bstlnk2 = BST()         # linked-based BST
        run(bstlnk2, n, True)   # average case
    print("{Array-based}")
    for i in range(4, 12, 1):
        n = 2**i
        bstarr2 = BST_ARRAY()   # array-based BST
        run(bstarr2, n, True)   # average case

if __name__ == "__main__":
    print("#1. linked based BST ===============================================")
    bst_link = BST()
    Check(bst_link)             # Check linked_based BST
    print("\n#2. array based BST ==============================================")
    bst_array = BST_ARRAY()
    Check(bst_array)            # Check array_based BST
    print("\n#3. Run Time Analysis ============================================")
    RunTimeAnalysis()           # Do Runtime Analysis

