class Empty(Exception):                     # Empty Exception
    pass

class ArrayQueue:                           # Double Ended Queue
    DEFAULT_CAPACITY = 10                   # initial Deque size

    def __init__(self):                     # create empty deque
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0                      # number of element
        self._front = 0                     # front index number

    def __len__(self):                      # return current # of element
        return self._size

    def is_empty(self):                     # return deque is empty or not
        return self._size == 0

    def first(self):                        # peek the front element
        if self.is_empty():                 # empty check
            raise Empty('Queue is empty')
        return self._data[self._front]      

    def last(self):                         # peek the last element
        if self.is_empty():                 # empty check
            raise Empty('Queue is empty')
        lastidx = (self._front + self._size - 1) % len(self._data)
        return self._data[lastidx]          

    def _dequeue(self):                     # dequeue == delete first
        if self.is_empty():                 # empty check
            raise Empty('Queue is empty')
        answer = self._data[self._front]    # get front element
        self._data[self._front] = None      # remove front data
        self._front = (self._front + 1) % len(self._data)   # update front
        self._size -= 1                     # update size
        return answer

    def _enqueue(self, e):                  # enqueue == add last 
        if self._size == len(self._data):   # full check
            self._resize(2*len(self._data)) # if full, doubling the size
        avail = (self._front + self._size) % len(self._data)    # idx of last
        self._data[avail] = e               # insert element
        self._size += 1                     # update size

    def _resize(self, cap):                 # method for size extand
        old = self._data                    # copy old data
        self._data = [None]*cap             # reset and resize the data array
        walk = self._front                  # copy index (from front)
        for k in range(self._size):         # paste old data to new object
            self._data[k] = old[walk]       # using copy index 'walk'
            walk = (walk + 1) % len(old)
        self._front = 0                     # reset the front value

    def add_first(self, e):                 # insert elemnt @ front-1
        if self._size == len(self._data):   # full check
            self._resize(2*len(self._data)) # if full, doubling the size
        self._front = (self._front - 1) % len(self._data)   # front update
        self._data[self._front] = e         # insert
        self._size += 1                     # update size

    def add_last(self, e):                  # insert element @ last
        ArrayQueue._enqueue(self, e)        # == enqueue()
    
    def delete_first(self):                 # delete element @ front
        return ArrayQueue._dequeue(self)    # == dequeue()

    def delete_last(self):                  # delete element @ last
        if self.is_empty():                 # empty check
            raise Empty('Queue is empty')
        delidx = (self._front + self._size - 1) % len(self._data)
        answer = self._data[delidx]         # get last element
        self._data[delidx] = None           # remove last data
        self._size -= 1                     # update size
        return answer

def isPalindrome_DEQue(string):             # check string is Palindrome
    strsize = len(string)                   # string size
    addend = int(strsize/2)                 # half index for add
    queue = ArrayQueue()                    # create deque object
    for i in range(addend):                 # from 0 to half index, add last
        queue.add_last(string[i])
    delstart = int((strsize+1)/2)           # half index for delete
    for j in range(delstart, strsize):      # from half index to end, dequeue
        if string[j] != queue.delete_last():# and compare     
            return False                    # break and return False
    return True                             # return True

from time import time
from HW1_2_2015311951 import ArrayStack
from HW1_2_2015311951 import isPalindrome_Stack 
def ExcuteTime(n):                              # compare acture running time
    string = " "*n                              # make n size simple palindrome string
    startS = time()
    isP = isPalindrome_Stack(string)
    endS = time()
    timeS = round((endS - startS)*1000000, 3)   # stack running time (us)
    startQ = time()
    isP = isPalindrome_DEQue(string)
    endQ = time()
    timeQ = round((endQ - startQ)*1000000, 3)   # deque running time (us)
    return n, timeS, timeQ                      

def DEBUG():                # this procedure is not for HW but debugging my code
    print(isPalindrome_DEQue("TENET"))      # odd True
    print(isPalindrome_DEQue("TENNET"))     # even True 
    print(isPalindrome_DEQue("MULAN"))      # odd False
    print(isPalindrome_DEQue("MULLAN"))     # even False

def EXPERIMENT():           # compare stack/deque palindrome checker running time
    print("(n, Stack(us), DEQue(us))")      
    for i in range(2, 9):                   
        n = 10**i                           # for n = 10^2 to 10^8
        print(ExcuteTime(n))                # print acture running time

if __name__ == '__main__':
    # DEBUG()
    EXPERIMENT()
    print(isPalindrome_DEQue(input("user's string: "))) # User input test    

