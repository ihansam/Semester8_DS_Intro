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

if __name__ == "__main__":
    print("[n, double(us), incremental(us)]")
    for i in range(2, 9):           # n = from 10^2 to 10^8
        n = 10**i
        runtime_d = round(compute_average(n)*1000000, 3)        # dynamic
        runtime_i = round(compute_inc_average(n)*1000000, 3)    # incremental
        print([n, runtime_d, runtime_i])                        # print runtime
# ===========================================
