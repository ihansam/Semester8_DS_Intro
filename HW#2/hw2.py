#1. Linked-Based BST
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key    = key
        self.value  = value
        self.left   = left
        self.right  = right

class LinkedBST:                # Linked Structure Binary Search Tree
    def __init__(self):         # Empty BST initialize
        self.root = None        

    # [SEARCH]
    def get(self, k):           # get value of key
        print(self._get_item(self.root, k)) # search from the root node

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
    def _min(self):     # find min node
        if self.root == None:
            return None
        return self._minimum(self.root)

    def _minimum(self, n):
        if n.left == None:  # min node found
            return n
        return self._minimum(n.left)    # else go left

    def delete_min(slef):   # delete minumum node
        if self.root == None:
            print("Tree is Empty")
        self.root = self._del_min(self.root)
        
    def _del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self._del_min(n.left)
        return n

    def delete(self, k):
        self.root = self._del_node(self.root, k)
    
    def _del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self._del_node(n.left, k)
        elif n.key > k:
            n.right = self._del_node(n.right, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self._minimum(target.right)
            n.right = self._del_min(target.right)
            n.left = target.left
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
        print()

def CheckLinkBST():
    lt = LinkedBST()
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

def CheckArrayBST():
    pass

def RunTimeAnalysis():
    pass

if __name__ == "__main__":
    CheckLinkBST()
    CheckArrayBST()
    RunTimeAnalysis()

