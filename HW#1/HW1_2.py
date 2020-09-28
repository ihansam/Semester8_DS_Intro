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
def isPalindrome_Stack(string):
    strsize = len(string)
    pushend = int(strsize/2)
    stack = ArrayStack()
    for i in range(pushend):
        stack.push(string[i])
    popstart = int((strsize+1)/2)
    for j in range(popstart, strsize):
        if string[j] != stack.pop():
            return False
    return True

if __name__ == '__main__':
    print(isPalindrome_Stack("TENET"))
    print(isPalindrome_Stack("TENNET"))
    print(isPalindrome_Stack("MULAN"))
    print(isPalindrome_Stack("MULLAN"))
    print(isPalindrome_Stack(input("user's string: ")))
# =================================================
