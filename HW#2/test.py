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
    
    def __str__(self):              # for check array elements
        return 'KEY: ' + str(self._keydata) + '\nVAL: ' + str(self._valdata)

    def isEmpty(self):              # check Empty or not
        try:
            return self._keydata[0] == None
        except:
            return True

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

    # [DELETE]
    def _rightChildPromote(self, root): # delete root and promote right child   <= Need to Delete
        if self._keydata[left(root)] == None:   # when left child is empty
            self._nodePromote(right(root), root)
    
    def _nodePromote(self, where, to):  # node promote recursively
        key = self._keydata[where]      # save where node 
        val = self._valdata[where]       
        self._keydata[to] = key         # replace to node
        self._valdata[to] = val         
        self._keydata[where] = None     # delete where node
        self._valdata[where] = None
        if (left(where) < len(self._keydata)):  # next depth exist check
            if(self._keydata[left(where)] != None):     # go left if exist
                self._nodePromote(left(where), left(to))
            if(self._keydata[right(where)] != None):    # go right if exist
                self._nodePromote(right(where), right(to))

    def _minimum(self, start):          # find minimun node
        idx = start                     # from start index
        if self._keydata[idx] == None:  # Empty case return
            return None
        size = len(self._keydata)       # until meet None or Undefined node
        while (idx < size and self._keydata[idx] != None):
            idx = left(idx)             # go left
        return parent(idx)              # and return index

    def delete(self, key):              # delete node by key
        n, v, idx = self._get(key)      # find delete node
        if n == key:                    # if delete node exist
            if (left(idx) >= len(self._keydata)):
                self._keydata[idx] = None
                self._valdata[idx] = None
            elif (self._keydata[left(idx)] == None):
                self._nodePromote(right(idx), idx)
            elif (self._keydata[right(idx)] == None):
                self._nodePromote(left(idx), idx)
            else:
                successor = self._minimum(right(idx))
                self._keydata[idx] = self._keydata[successor]
                self._valdata[idx] = self._valdata[successor]
                self._keydata[successor] = None
                self._valdata[successor] = None
                try:
                    if(self._keydata[right(successor)] != None):
                        self._nodePromote(right(successor), successor)
                except:
                    pass
    
    # [Treversal]
    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def levelorder(self):
        print(self)

if __name__ == "__main__":
    bst = BST_ARRAY()
    array = [11, 4, 16, 1, 9, 14, 19, 6, 15, 5, 7]
    for item in array:
        bst.put(item, item)
    bst.delete(4)
    bst.delete(11)
    bst.delete(9)
    bst.delete(7)
    bst.delete(14)
    print(bst)
