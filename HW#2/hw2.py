class Node:
    def __init__(self, key, value, ledt=None, right=None):
        self.key    = key
        self.value  = value
        self.left   = left
        self.right  = right
        self.item   = (key, value)

#1. Linked-based BST
class BST:
    def __init__(self):         # Make Tree
        self.root = None        # tree root

    # [SEARCH]
    def get(self, key):         
        return self._get_item(self.root, k) # start from root

    def _get_item(self, n, k):  # compare node, key
        if n == None:           # no such key in Tree
            return None
        if n.key > k:           # smaller target, go left
            return self._get_item(n.left, k)
        elif n.key < k:         # larger target, go right
            return self._get_item(n.right, k)
        else:                   # find target
            return n.value

    # [INSERT]
    def put(self, key, value):
        self.root = self._put_item(self.root, key, value)   # start from root

    def _put_item(self, n, key, value):
        if n == None:
            return Node(key, value) # make new node to n
        if n.key > key:             # smaller key, go left
            n.left = self._put_item(n.left, key, value)
        elif n.key < key:           # larger key, go right
            n.right = slef._put_item(n.right, key, value)
        else:                       # already key exist
            n.value = value
        return n                    # return the node

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

    def preorder(self, n):
        if n != None:
            print(str(n.item), ' ', end = ' ')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item), ' ', end=' ')

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item), ' ', end=' ')
            if n.right:
                self.inorder(n.right)

    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item), ' ', end=' ')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

def CheckLinkBST():
    pass
    print("hello")

def CheckArrayBST():
    pass
    print("world")

def RunTimeAnalysis():
    pass
    print("!!!!!")

if __name__ == "__main__":
    CheckLinkBST()
    CheckArrayBST()
    RunTimeAnalysis()

