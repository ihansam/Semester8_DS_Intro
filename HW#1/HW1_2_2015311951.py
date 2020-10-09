class Empty(Exception):                     # Empty Exception
    pass

class ArrayStack:                           # Stack using Python list
    
    def __init__(self):                     # Create Empty stack
        self._data = []

    def __len__(self):                      # return # of elments
        return len(self._data)

    def is_empty(self):                     # return empty or not
        return len(self._data) == 0

    def push(self, e):                      # push 'e' on the top
        self._data.append(e)

    def top(self):                          # peek a top element
        if self.is_empty():                 # empty check
            raise Empty('Stack is empty')
        return self._data[-1]               # last appended element

    def pop(self):                          # remove and return the top element
        if self.is_empty():                 # empty check
            raise Empty('Stack is empty')
        return self._data.pop()

# =================================================
def isPalindrome_Stack(string):             # check string is Palindrome
    strsize = len(string)                   # string size
    pushend = int(strsize/2)                # half index for push
    stack = ArrayStack()                    # create stack object
    for i in range(pushend):                # from 0 to half index, push
        stack.push(string[i])
    popstart = int((strsize+1)/2)           # half index for pop
    for j in range(popstart, strsize):      # from half index to end, pop
        if string[j] != stack.pop():        # and compare
            return False                    # break and return False
    return True                             # return True

if __name__ == '__main__':                  # for test
    # print(isPalindrome_Stack("TENET"))      # odd True
    # print(isPalindrome_Stack("TENNET"))     # even True 
    # print(isPalindrome_Stack("MULAN"))      # odd False
    # print(isPalindrome_Stack("MULLAN"))     # even False
    print(isPalindrome_Stack(input("user's string: "))) # User input test
# =================================================
