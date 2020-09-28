# HW#1 JKD, ver 1.0 define classes
# 1 Dynamic Array ===============================================================
import ctypes                       # for using array

class DynamicArray:
    # ===========================================
    C = 100     # constant for incremental replacement
    # ===========================================
 
    def __init__(self):                             # Create Empty Array
        self._n = 0                                 # Current # of element
        self._capacity = 1                          # Capacity 
        self._A = self._make_array(self._capacity)  # Array Object

    def __len__(self):                              # return 'n'
        return self._n                              
    
    def __getitem__(self, k):                       # return kth element
        if not 0 <= k < slef._n:                    # index check
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):                          # append using doubling
        if self._n == self._capacity:               # when array is full
            self._resize(2*self._capacity)          # double size 
        self._A[self._n] = obj                      # append new element
        self._n += 1                                # n = n+1

    # ===========================================
    def append_incremental(self, obj):              # append using incremental
        if self._n == self._capacity:
            self._resize(self._capacity + DynamicArray.C)   # expand constant 'C'
        self._A[self._n] = obj
        self._n += 1
    # ===========================================
 
    def _resize(self, c):                           # expand size
        B = self._make_array(c)                     # c size new Array
        for k in range(self._n):                    # old Array copy
            B[k] = self._A[k]
        self._A = B                                 # paste
        self._capacity = c                          # set size = c

    def _make_array(self, c):                       # make c size Array object
        return (c*ctypes.py_object)()

from time import time
def compute_average(n):     # compute aveage running time for a doubling append
    data = DynamicArray()           # empty Dynamic array
    start = time()                  # record start time
    for k in range(n):              # append n time
        data.append(None)           # (empty element)
    end = time()                    # record end time
    return (end - start)/n          # calculate avg time (in seconds)

# ===========================================
def compute_inc_average(n): # compute aveage running time for a incre-append
    data = DynamicArray()           # empty Dynamic array
    start = time()                  # record start time
    for k in range(n):              # append n time
        data.append_incremental(None)
    end = time()                    # record end time
    return (end - start)/n          # calculate avg time (in seconds)
# ===========================================
 
# HW1 main #
print("[n, double(us), incremental(us)]")
for i in range(2, 9):
    n = 10**i
    runtime_d = round(compute_average(n)*1000000, 3)
    runtime_i = round(compute_inc_average(n)*1000000, 3)
    print([n, runtime_d, runtime_i])



# 2 Stack =======================================================================
class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0












